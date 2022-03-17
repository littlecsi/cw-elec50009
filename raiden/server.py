from multiprocessing import connection
import socket

class Server:
    player1_address = ("", 13000)
    player2_address = ("", 14000)
    def __init__(self, server="", server_port=12000) -> None:
        self.server = server
        self.server_port = server_port

        # Create a welcome socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Bind the server to the localhost
        self.server_socket.bind((self.server, self.server_port))

        # Ready message
        print("Game server running on port ", self.server_port)

        # print("Waiting for Player 1")
        # self.player1_ip = self.server_socket.recvfrom(1024)

        # print("player1 info :", self.player1_add)

        # print("Waiting for Player 2")
        # self.player2_ip = self.server_socket.recvfrom(1024)
        # self.player2_add = (self.player2_ip, 15000)

        # Main server loop
        while True:
            cmsg, cadd = self.server_socket.recvfrom(1024)
            print("Received :", cmsg.decode(), "from :", cadd)

            if self.player1_address[0] == "":
                self.player1_address = (cmsg.decode(), 13000)
                
                smsg = "IP address received."
                self.respond(smsg, cadd)

            else:
                self.respond("HELLO", cadd)
                pass
            
    def respond(self, smsg, cadd):
        self.server_socket.sendto(smsg.encode(), cadd)
        print("Sent : ", smsg, ", to : ", cadd)
            
def main():
    server = Server()


if __name__ == '__main__':
    main()