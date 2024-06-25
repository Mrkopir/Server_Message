import socket

class Client:
    def __init__(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def client_connect(self):
        self._client.connect(('localhost', 52324))