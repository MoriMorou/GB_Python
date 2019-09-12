from argparse import ArgumentParser
import json

import config as config
import yaml
import socket
import logging
from datetime import datetime

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

# Логирование
logger = logging.getLogger('client')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('client.log')

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

try:
    sock = socket.socket()
    sock.connect((host, port))
    logger.debug(f'Client started with {host}:{port}')
    action = input('Enter Action: ')
    data = input('Enter data: ')
    request = {
        'action': action,
        'data': data,
        'time': datetime.now().timestamp()
    }
    s_request = json.dumps(request)
    sock.send(s_request.encode(encoding))
    response = sock.recv(buffersize)
    print(response.decode(encoding))
    logger.debug(f'{response.decode(encoding)}')
except KeyboardInterrupt:
    pass