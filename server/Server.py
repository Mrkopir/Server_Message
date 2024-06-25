import socket

class Server:
    def __init__(self):
        self.__host='localhost'
        self.__port=52324

        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind((self.__host, self.__port))

    def start_server(self):
        self._server.listen()
        print("Server is working...")

