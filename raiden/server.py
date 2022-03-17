from multiprocessing import connection
import socket

class Server:
    player1_ip = ""
    player2_ip = ""
    def __init__(self, server="0.0.0.0", port=12000) -> None:
        self.server = server
        self.port = port

        # Create a welcome socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Bind the server to the localhost
        self.server_socket.bind((self.server, self.port))
        self.server_socket.listen(1)

        # Ready message
        print("Server running on port ", self.port)

        self.server_conn, caddr = self.server_socket.accept()

        print("Waiting for Player 1")
        self.player1_ip = self.server_conn.recvfrom(1024)
        self.player1_add = (self.player1_ip, 14000)

        # print("Waiting for Player 2")
        # self.player2_ip = self.server_conn.recvfrom(1024)
        # self.player2_add = (self.player2_ip, 15000)

        # Main server loop
        while True:
            self.connection_socket, caddr = self.welcome_socket.accept()

            self.cmsg = self.connection_socket.recv(1024)
            self.cmsg = self.cmsg.decode()
            print("Before sending")

            self.connection_socket.send(self.cmsg.encode())
            print("After sending back")
            # if(cmsg.isalnum() == False): 
            #     cmsg = "Not alphanumeric."; 
            # else: 
            #     cmsg = "Alphanumeric"; 
            # connection_socket.send(cmsg.encode())

    def print_msg(self, msg) -> None:
        print(msg)
        return None

def main():
    server = Server()


if __name__ == '__main__':
    main()