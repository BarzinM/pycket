import socket


def my_ips():
    from subprocess import check_output
    raw = check_output(['hostname', '--all-ip-addresses'])
    ips = raw.decode("utf-8")
    ips = ips.strip().split()
    return ips


def pingable(ip):
    import os
    response = os.system("ping -c 1 " + ip + " >/dev/null")
    if response == 0:
        return True
    else:
        return False


class TCP(object):

    def __init__(self, ip='localhost', port=8089, type=None, backlog=0):
        self.ip = ip
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        if type is None:
            if ip in my_ips():
                print("TCP object being set as server!")
                self.sock.bind((self.ip, self.port))
                self.sock.listen(backlog)
                self.connection, address = self.sock.accept()
            elif pingable(ip):
                print("TCP object being set as client!")
                self.sock.connect((self.ip, self.port))
                self.connection = self.sock
            else:
                raise ConnectionError(
                    "Couldn't locate ip %s" % ip)

        if type is not None:
            if type.lower() == "server":
                self.sock.bind((self.ip, self.port))
                self.sock.listen(backlog)
                self.connection, address = self.sock.accept()
            elif type.lower() == "client":
                self.sock.connect((self.ip, self.port))
                self.connection = self.sock
            else:
                raise TypeError(
                    "Possible input values for argument `type` are either 'server' or 'client'.")

    def server(self, backlog=0):
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

    def timeout(self, time):
        self.connection.settimeout(time)
