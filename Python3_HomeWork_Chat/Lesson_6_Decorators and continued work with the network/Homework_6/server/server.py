import yaml
import json
import socket
import logging

from argparse import ArgumentParser
from actions import resolve
from handlers import handle_default_request
from protocol import (
    validate_request,
    make_response,
)

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file'
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

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('server.log', encoding=encoding),
        logging.StreamHandler()
    ]
)

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    logging.info(f'server started with {host}:{port}')

    while True:
        client, address = sock.accept()
        logging.info(f'Client was started {address[0]}:{address[1]}')
        b_request = client.recv(buffer_size)
        b_response = handle_default_request(b_request)
        client.send(b_response)
        client.close()
except KeyboardInterrupt:
    pass