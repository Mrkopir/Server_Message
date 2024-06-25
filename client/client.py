import socket

class Client:
    def __init__(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def client_connect(self):
        self._client.connect(('localhost', 52324))

class ClientСonnect(Client):
    def __init__(self):
        super().__init__()
        self.__message = None
        self.__data = None

    def send_data(self):
        self.client_connect()

        self.__data = self._client.recv(1024)

        print(self.__data.decode("utf-8"))

        while True:
            self.__message = input(">>> ")
            self._client.send(self.__message.encode("utf-8"))


CL = ClientСonnect()
CL.send_data()