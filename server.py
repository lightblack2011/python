from socket import *
import argparse

Connection = socket(AF_INET, SOCK_STREAM)
parser = argparse.ArgumentParser()
parser.add_argument('-a', default=gethostname())
parser.add_argument('-p', type=int, default='7777')
ConnectionParsed = parser.parse_args()
HOST = ConnectionParsed.a
PORT = ConnectionParsed.p
sock = socket()
sock.bind((HOST, PORT))
print(f"Server started on host = {HOST}, port = {PORT}")
while True:
    sock.listen(10)
