import socket


class TCP(object):

    def __init__(self, ip='localhost', port=8089):
        self.ip = ip
        self.port = port

        self.server_set = False

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def server(self, backlog=1):
        if not self.server_set:
            self.sock.bind((self.ip, self.port))
            self.sock.listen(backlog)
        self.connection, address = self.sock.accept()
        return self.connection

    def client(self):
        self.sock.connect((self.ip, self.port))
        self.connection = self.sock
        return self.connection

    def recv(self, length=4096):
        return self.connection.recv(length)

    def send(self, data):
        self.connection.sendall(data)
