import sys
import json
import multiprocessing
import subprocess

def start_server(ip, port, showUI):
    try:
        print(ip, port, showUI)
        subprocess.run(["python", "server.py", str(ip), str(port), str(showUI)])
    except:
        subprocess.run(["python3", "server.py", str(ip), str(port), str(showUI)])

def start_client():
    try:
        subprocess.run(["python", "client.py"])
    except:
        subprocess.run(["python3", "client.py"])

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

    if 'r' in params['mode']:
        client_process = multiprocessing.Process(target=start_client)
        client_process.start()
        client_process.join()
    if 's' in params['mode']:
        server_process = multiprocessing.Process(target=start_server, args=(params["IP","Port",True]))
        server_process.start()
        server_process.join()

if __name__ == '__main__':
    main()