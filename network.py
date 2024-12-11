import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "" #LocalSeverIP
        self.port = 5555
        self.address = (self.server, self.port)
        self.p = self.connect()

    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)

    def getP(self):
        return self.p
