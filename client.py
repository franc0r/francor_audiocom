import sys
import socket, cv2, pickle,struct,time
import pyshine as ps

class AudioClient:

	def __init__(self, host_ip, port, showui=False):
		mode =  'get'
		name = 'CLIENT RECEIVING AUDIO'
		self.audio,context = ps.audioCapture(mode=mode)
		if showui:
			ps.showPlot(context,name)

		# create socket
		self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		port = 4982

		socket_address = (host_ip,port)
		self.client_socket.connect(socket_address) 
		print("CLIENT CONNECTED TO",socket_address)

	def run(self):
		
		data = b""
		payload_size = struct.calcsize("Q")
		while True:
			while len(data) < payload_size:
				packet = self.client_socket.recv(4*1024) # 4K
				if not packet: break
				data+=packet
			packed_msg_size = data[:payload_size]
			data = data[payload_size:]
			msg_size = struct.unpack("Q",packed_msg_size)[0]
			
			while len(data) < msg_size:
				data += self.client_socket.recv(4*1024)
			frame_data = data[:msg_size]
			data  = data[msg_size:]
			frame = pickle.loads(frame_data)
			self.audio.put(frame)

			self.client_socket.close()

if __name__ == '__main__':
	params = sys.argv[1:]
	audio_client = AudioClient(*params)
	audio_client.run()