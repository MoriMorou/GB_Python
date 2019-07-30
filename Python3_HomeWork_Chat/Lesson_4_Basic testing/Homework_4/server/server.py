from argparse import ArgumentParser

import config as config
import yaml
import json
import socket

from actions import resolve
from protocol import (
    validate_request,
    make_response,
)

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file'
    # required = True
)

args = parser.parse_args()

host = 'localhost'
port = 8088
buffersize = 1024
encoding = 'utf-8'

if args.config:
    with open(args.config) as file:
        config = yaml.load(config.yml, Loader=yaml.Loader)
        host = config.get('host')
        port = config.get('port')
        buffersize = config.get('buffersize')
        encoding = config.get('encoding')


try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    print(f'Server was started with {host}:{port}')


    while True:
        client, address = sock.accept()

        b_request = client.recv(buffersize)
        request = json.loads(b_request.decode(encoding))

        if validate_request(request):
            action_name = request.get('action')
            controller = resolve(action_name)
            if controller:
                try:
                    response = controller(request)
                except Exception as err:
                    print(err)
                    response = make_response(request, 500, 'Internal server error')
            else:
                response = make_response(request, 404, 'Action not found')
        else:
            make_response(request, 400, 'Wrong request')
        s_response = json.dumps(response)
        client.send(s_response.encode(encoding))
        client.close()
except KeyboardInterrupt:
    pass