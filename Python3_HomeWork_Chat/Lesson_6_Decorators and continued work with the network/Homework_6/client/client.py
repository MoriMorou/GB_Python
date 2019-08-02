import zlib
import json
import yaml
import socket
import hashlib
import logging
from datetime import datetime
from argparse import ArgumentParser

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
        # Создаем файловый обработчик логирования (можно задать корректировку)
        logging.FileHandler('client.log', encoding=encoding),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('client')

try:
    sock = socket.socket()
    sock.connect((host, port))
    print('Client started')
    logger.debug(f'Client started with {host}:{port}')
    action = input('Enter Action: ')
    data = input('Enter data: ')

    hash_obj = hashlib.sha256()
    hash_obj.update(
        str(datetime.now().timestamp()).encode(encoding)
    )

    request = {
        'action': action,
        'data': data,
        'time': datetime.now().timestamp(),
        'user': hash_obj.hexdigest()
    }
    s_request = json.dumps(request)
    b_request = zlib.compress(s_request.encode(encoding))
    sock.send(b_request)
    response = sock.recv(buffer_size)
    b_response = zlib.decompress(response)
    print(b_response.decode(encoding))
    logger.debug(f'{b_response.decode(encoding)}')
except KeyboardInterrupt:
    pass

