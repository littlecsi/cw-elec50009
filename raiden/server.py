from multiprocessing import connection
import socket

class Server:
    def __init__(self, server="0.0.0.0", port=12000) -> None:
        self.server = server
        self.port = port

        # Create a welcome socket
        self.welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the server to the localhost
        self.welcome_socket.bind((self.server, self.port))
        self.welcome_socket.listen(1)

        # Ready message
        print("Server running on port ", self.port)

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