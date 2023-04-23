import sys
import json
import multiprocessing
import subprocess

def start_server(ip, port, showui):
    try:
        subprocess.run(["python", "server.py", str(ip), str(port), str(showui)])
    except:
        subprocess.run(["python3", "server.py", str(ip), str(port), str(showui)])

def start_client(ip, port, showui):
    try:
        subprocess.run(["python", "client.py", str(ip), str(port), str(showui)])
    except:
        subprocess.run(["python3", "client.py", str(ip), str(port), str(showui)])

def follow_routine_basestation():
    pass

def follow_routine_robot():
    pass


def main():
    configName = "config.json"
    params = json.load(open(configName))[sys.argv[1]]
    print(params)
    if "Empty" == sys.argv[1]:
        print("started dummy process")

    if 's' in params['mode']:
        server_process = multiprocessing.Process(target=start_server, args=(params["HostIP"],params["Port"],True))
        server_process.start()
        server_process.join()        
    if 'r' in params['mode']:
        client_process = multiprocessing.Process(target=start_client, args=(params["ReceiverIP"],params["Port"],True))
        client_process.start()
        client_process.join()

if __name__ == '__main__':
    main()