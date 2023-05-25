import socket
import  datetime
import threading

PORT = 7500
BUFSIZE = 4096

def client_handler(client,addr):
    while True:
        try: