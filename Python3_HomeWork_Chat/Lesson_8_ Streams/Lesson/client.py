import zlib
import json
import yaml
import socket
import threading
from datetime import datetime
from argparse import ArgumentParser

WRITE_MODE = 'write'

READ_MODE = 'read'

def read(sock, buffersize):
    while True:
        response = sock.recv(buffersize)
        bytes_response = zlib.decompress(response)
        print(bytes_response.decode())


def make_request(action, data):
    return {
        'action': action,
        'time': datetime.now().timestamp(),
        'data': data,
    }

parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str, required=False,
    help='Sets config file path'
)

args = parser.parse_args()

config = {
    'host': 'localhost',
    'port': 8088,
    'buffersize': 1024
}

if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        config.update(file_config)

host, port = config.get('host'), config.get('port')

try:
    sock = socket.socket()
    sock.connect((host, port))
    print('Clien was started')

    read_thread = threading.Thread(
        target=read, args=(sock, config.get('buffersize'))
    )
    read_thread.start()

    while True:
        action = input('Enter action: ')
        data = input('Enter data: ')

        request = make_request(action, data)
        str_request = json.dumps(request)
        bytes_request = zlib.compress(str_request.encode())
        
        sock.send(bytes_request)
        print(f'Client send data { data }')
except KeyboardInterrupt:
    print('client shutdown.')