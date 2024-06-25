import threading

from Listener import Listener

class MainServerClass(Listener):
    def __init__(self):
        super().__init__()

    def run(self):
        self.start_server()
        self.accept_clients()

server = MainServerClass()
server_thread = threading.Thread(target=server.run)
server_thread.start()

