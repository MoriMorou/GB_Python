import yaml
import socket
import logging
import select
import threading

from argparse import ArgumentParser
from handlers import handle_default_request


def read(client, requests, buffersize):
    b_request = client.recv(buffersize)
    requests.append(b_request)

def write(client, response):
    client.send(response)

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
        logging.FileHandler('main.log', encoding=encoding),
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
    logging.info(f'server started with {host}:{port}')

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
                rthread = threading.Thread(target=read, args=(r_client, requests, buffer_size))
                rthread.start()


            if requests:
                b_request = requests.pop()
                b_response = handle_default_request(b_request)

                for w_client in wlist:
                    wthread = threading.Thread(target=write, args=(w_client, b_response))
                    wthread.start()

except KeyboardInterrupt:
    pass