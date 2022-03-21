import socket
import awsdb as db

class Server:
    def __init__(self, server="", server_port=12000) -> None:
        self.server = server
        self.server_port = server_port

        # Create a welcome socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bind the server to the localhost
        self.server_socket.bind(("", self.server_port))

        self.server_socket.listen(1)

        # Ready message
        print("Game server running on port ", self.server_port)

        # Main server loop
        while 1:
            self.connection_socket, cadd = self.server_socket.accept()

            cmsg = self.connection_socket.recv(1024)
            print("Received :", cmsg.decode())
            self.respond("RECEIVED")

            if cmsg.decode() == "END":
                print("CHECKPOINT")
                self.connection_socket, cadd = self.server_socket.accept()
                name = self.connection_socket.recv(1024)
                self.respond("RECEIVED")

                self.connection_socket, cadd = self.server_socket.accept()
                score = self.connection_socket.recv(1024)
                self.respond("RECEIVED")

                self.connection_socket, cadd = self.server_socket.accept()
                date = self.connection_socket.recv(1024)
                self.respond("RECEIVED")

                db.put_score(name.decode(), int(score.decode()), date.decode())

                highest_score = db.get_highest_score()
                self.respond(str(highest_score))
            
    def respond(self, smsg):
        self.connection_socket.send(smsg.encode())
        print("Sent : ", smsg)
            
def main():
    server = Server()

if __name__ == '__main__':
    main()