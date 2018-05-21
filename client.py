from socket import *
import argparse


Connection = (AF_INET, SOCK_STREAM)
parser = argparse.ArgumentParser()
parser.add_argument('-addr')
parser.add_argument('-port', default='7777')
ConnectionParsed = parser.parse_args()
HOST = ConnectionParsed.addr
PORT = ConnectionParsed.port



