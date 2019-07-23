import argparse
import yaml
import socket
import json

# загружаем константы
from settings import HOST, PORT, BUFFERSIZE, ENCODING, MAX_CLIENTS

host = HOST
port = PORT
buffersize = BUFFERSIZE
encoding = ENCODING
max_clients = MAX_CLIENTS

# обрабатываем ключи запуска сервера
parser = argparse.ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Config file.'
)
parser.add_argument(
    '-p', '--port', type=int,
    help='Port.'
)
parser.add_argument(
    '-a', '--addr', type=str,
    help='IP-address.'
)
args = parser.parse_args()

# если указан файл конфигурации, то переопределяем указанные в нём переменные, остальные неизменны
# если указан файл конфигурации, то все остальные ключи запуска игнорируются
if args.config:
    with open(args.config) as file:
        conf = yaml.load(file, Loader=yaml.Loader)
        host = conf.get('host', HOST)
        port = conf.get('port', PORT)
        buffersize = conf.get('buffersize', BUFFERSIZE)
        encoding = conf.get('encoding', ENCODING)
        max_clients = conf.get('max_clients', MAX_CLIENTS)
else:
    if args.port:
        port = args.port
    if args.addr:
        host = args.addr

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(max_clients)
    print('The server is running and waiting for connections ...')

    while True:
        client, address = sock.accept()
        print(f'New client connected from address {address}.')

        b_data = client.recv(buffersize)
        request = json.loads(b_data.decode(encoding))
        response = json.dumps(request)
        client.send(response.encode(encoding))

        client.close()
        print(f'Client {address} disconnected.')

except KeyboardInterrupt:
    print('Server stopped.')
