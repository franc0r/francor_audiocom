import sys
import json
import multiprocessing
import subprocess

def start_server():
    subprocess.run(["python", "server.py"])

def start_client():
    subprocess.run(["python", "client.py"])


def main():
    configName = "config.json"
    print(json.load(open(configName))[sys.argv[1]])
    server_process = multiprocessing.Process(target=start_server)
    client_process = multiprocessing.Process(target=start_client)
    server_process.start()
    client_process.start()
    server_process.join()
    client_process.join()

if __name__ == '__main__':
    main()