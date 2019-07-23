import argparse
import yaml
import socket
import json

# Загружаем константы
from settings import HOST, PORT, BUFFERSIZE, ENCODING

host = HOST
port = PORT
buffersize = BUFFERSIZE
encoding = ENCODING

# Обрабатываем ключи запуска сервера
parser = argparse.ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Config file.'
)
parser.add_argument(
    '-addr', '--address', type=str,
    help='IP-server address.'
)
parser.add_argument(
    '-p', '--port', type=int,
    help='Server port.'
)
args = parser.parse_args()

# Если указан файл конфигурации, то переопределяем указанные в нём переменные, остальные неизменны
# Если указан файл конфигурации, то остальные ключи запуска игнорируются
if args.config:
    with open(args.config) as file:
        conf = yaml.load(file, Loader = yaml.Loader)
        host = conf.get('host', HOST)
        port = conf.get('port', PORT)
        buffersize = conf.get('buffersize', BUFFERSIZE)
        encoding = conf.get('encoding', ENCODING)
else:
    if args.address:
        host = args.address
    if args.port:
        port = args.port

try:
    sock = socket.socket()
    sock.connect((host, port))
    print('The client is running. A connection to the server has been established.')

    data = input('Your message: ')
    request = json.dumps({'data': data})

    sock.send(request.encode(encoding))
    b_data = sock.recv(buffersize)
    response = json.loads(b_data.decode(encoding))

    print(response)

    sock.close()

except KeyboardInterrupt:
    print('Client is closed.')
except ConnectionRefusedError:
    print('The server rejected the request. Check your connection settings.')
except TimeoutError:
    print('Connection error.')