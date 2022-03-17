import ipaddress
import socket

class Client:
    def __init__(self, server="54.159.72.106", port=12000) -> None:
        self.server = server
        self.port = port
        
        # Create a TCP client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set up a TCP connection with the server
        # connection_socket will be assigned to this client on the server side
        self.client_socket.connect((self.server, self.port))
        print("Connected to Server!")

    def send_msg(self, data) -> str:
        # Send the message to the TCP server
        self.client_socket.send(data.encode())
        # Return values from the server
        msg = self.client_socket.recv(1024)
        
        return msg.decode()

    def send_client_detail(self):
        hostname = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)
        ## printing the hostname and ip_address
        self.send_msg(ip_address)

    def close_client(self) -> None:
        self.client_socket.close()
        return None