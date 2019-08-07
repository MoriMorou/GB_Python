import yaml
import socket
import logging
import select
import time
from argparse import ArgumentParser
from handlers import handle_default_request

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

requests = []
connections = []

try:
    sock = socket.socket()
    sock.bind((host, port))

    sock.setblocking(False)
    sock.listen(5)
    logging.debug(f'server started with {host}:{port}')

    while True:
        try:
            client, address = sock.accept()
            logging.info(f'Client with address {address} was detected.')
            connections.append(client)
        except:
            pass

        if connections:

            rlist, wlist, xlist = select.select(
                connections, connections, connections, 0
            )

            for r_client in rlist:
                b_request = r_client.recv(buffer_size)
                requests.append(b_request)

            if requests:
                b_request = requests.pop()
                b_response = handle_default_request(b_request)

                for w_client in wlist:
                    w_client.send(b_response)
except KeyboardInterrupt:
    pass
