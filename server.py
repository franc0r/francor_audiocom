import sys
import socket, cv2, pickle,struct,time
import pyshine as ps


class AudioServer:

	def __init__(self, host_ip, port, showui=False):
		mode =  'send'
		name = 'SERVER TRANSMITTING AUDIO'
		self.audio, context= ps.audioCapture(mode=mode)
		if showui:
			ps.showPlot(context,name)

		# Socket Create
		backlog = 5
		self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket_address = (host_ip,port)
		print('STARTING SERVER AT',socket_address,'...')
		self.server_socket.bind(socket_address)
		self.server_socket.listen(backlog)

	def run(self):
		while True:
			client_socket,addr = self.server_socket.accept()
			print('GOT CONNECTION FROM:',addr)
			if client_socket:

				while(True):
					frame = self.audio.get()
					
					a = pickle.dumps(frame)
					message = struct.pack("Q",len(a))+a
					client_socket.sendall(message)
					
			else:
				break

		client_socket.close()		


if __name__ == '__main__':
	params = sys.argv[1:]
	audio_server = AudioServer(*params)
	audio_server.run()