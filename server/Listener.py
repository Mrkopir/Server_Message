import threading

from Server import Server

class Listener(Server):
    __client = None
    __address = None

    def __new__(cls, *args, **kwargs):
        if not cls.__client:
            cls.__client = object.__new__(cls, *args, **kwargs)
        return cls.__client
    
    def __new__(cls, *args, **kwargs):
        if not cls.__address:
            cls.__address = object.__new__(cls, *args, **kwargs)
        return cls.__address
    
    def __init__(self):
        super().__init__()

        self.__data = None

    def accept_clients(self):
        while True:
            __client, __address = self._server.accept()
            self.clients.append(__client)
            print(f"Client is trying to connect from {__address}")

            client_thread = threading.Thread(target=self.handle_client, args=(__client, __address))
            client_thread.start()

    def handle_client(self, __client, __address):
        __client.send("You connected successfully".encode("utf-8"))
        while True:
            try:
                self.__data = __client.recv(1024).decode("utf-8")
                if not self.__data:
                    break
                print(f"Received from {__address}: {self.__data}")
                self.broadcast(f"Message from {__address}: {self.__data}", __client)
            except ConnectionResetError:
                break
        self.clients.remove(__client)
        __client.close()
