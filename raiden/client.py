import socket

class Client:
    server = "3.83.254.8"
    server_port = 12000
    def __init__(self) -> None:
        # Create a TCP client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client_socket.connect((self.server, self.server_port))

    def send_msg(self, data):
        # Send the message to the TCP server
        self.client_socket.send(data.encode())
        print("Sent :", data)
    
    def receive(self):
        msg = self.client_socket.recv(1024)
        print("Received :", msg.decode())
        return msg.decode()

    def close_client(self) -> None:
        self.client_socket.close()
        return None