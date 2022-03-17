import socket

class Client:
    server = "3.83.254.8"
    server_port = 12000
    def __init__(self, client_port=13000) -> None:
        self.client_port = client_port
        
        # Create a TCP client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.client_socket.bind(('', self.client_port))

        # Set up a TCP connection with the server
        # connection_socket will be assigned to this client on the server side
        # self.client_socket.connect(self.server, self.port)
        # print("Connected to Server!")

    def send_msg(self, data):
        # Send the message to the TCP server
        self.client_socket.sendto(data.encode(),(self.server, self.server_port))
        print("Sent :", data, "to :", (self.server, self.server_port))
        # Return values from the server
        smsg, sadd = self.client_socket.recvfrom(1024)
        print("Received :", smsg.decode(), ", from :", sadd)
    
    def receive(self):
        msg, sadd = self.client_socket.recvfrom(2048)
        msg = msg.decode()

        # print(msg)
        print("Received :", msg, "from :", (self.server, self.server_port))

    def send_client_detail(self):
        hostname = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)
        ## printing the hostname and ip_address
        self.send_msg(ip_address)

    def close_client(self) -> None:
        self.client_socket.close()
        return None