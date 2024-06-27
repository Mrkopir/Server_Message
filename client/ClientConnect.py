import threading

from Client import Client

class ClientСonnect(Client):
    def __init__(self):
        super().__init__()
        self.__message = None
        self.__data = None

    def get_data(self):
        while True:
            self.__data = self._client.recv(1024)
            if self.__data:
                print(self.__data.decode("utf-8"))

    def send_data(self):
        self.client_connect()
        threading.Thread(target=self.get_data, daemon=True).start()

        while True:
            self.__message = input(">>> ")
            self._client.send(self.__message.encode("utf-8"))