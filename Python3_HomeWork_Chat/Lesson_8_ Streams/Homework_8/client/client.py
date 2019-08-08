import zlib
import json
import yaml
import socket
import hashlib
import threading

from datetime import datetime
from argparse import ArgumentParser


def read():
    while True:
        response = sock.recv(buffer_size)
        b_response = zlib.decompress(response)
        print(b_response.decode(encoding))


def write():
    while True:
        hash_obj = hashlib.sha256()
        hash_obj.update(
            str(datetime.now().timestamp()).encode(encoding)
        )

        action = input('Enter action: ')
        data = input('Enter data: ')

        request = {
            'action': action,
            'data': data,
            'time': datetime.now().timestamp(),
            'user': hash_obj.hexdigest()
        }
        s_request = json.dumps(request)
        b_request = zlib.compress(s_request.encode(encoding))
        sock.send(b_request)



parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file'
)

parser.add_argument(
    '-m', '--mode', type=str, default='rw',
    help='Sets client mode'
)

args = parser.parse_args()

host = 'localhost'
port = 8088
buffer_size = 1024
encoding = 'utf-8'

if args.config:
    with open(args.config) as file:
        config = yaml.load(config.yml, Loader=yaml.Loader)
        host = config.get('host')
        port = config.get('port')
        buffer_size = config.get('buffer_size')
        encoding = config.get('encoding')



try:
    sock = socket.socket()
    sock.connect((host, port))

    print(f'Client started: {host}:{port}')

    if args.mode == 'w':
       write()
    elif args.mode == 'rw':
        rthread = threading.Thread(target=read, daemon=True)
        rthread.start()
        write()
    else:
       read()

except KeyboardInterrupt:
    pass