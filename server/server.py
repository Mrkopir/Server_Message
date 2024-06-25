import socket
import threading

class Server:
    def __init__(self, host='localhost', port=52324):
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind((host, port))

    def start_server(self):
        self._server.listen()
        print("Server is working...")

    def accept_clients(self):
        while True:
            client_socket, client_address = self._server.accept()
            print(f"Client connected from {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        client_socket.send("You connected successfully".encode("utf-8"))
        while True:
            try:
                data = client_socket.recv(1024).decode("utf-8")
                if not data:
                    break
                print(f"Received: {data}")
            except ConnectionResetError:
                break
        client_socket.close()

class GetData(Server):
    def __init__(self, host='localhost', port=52324):
        super().__init__(host, port)

    def get_data(self):
        self.start_server()
        self.accept_clients()

server = GetData()
server_thread = threading.Thread(target=server.get_data)
server_thread.start()
