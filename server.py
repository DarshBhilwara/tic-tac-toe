import socket
from _thread import * 

server = ""
port = 9999

my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    my_server.bind((server, port))
except socket.error as e:
    print(str(e))

my_server.listen(2) #Refers to how many players can connect to the server at once
print("Server has started")

def threaded(connection, player):
    connection.send() #DewItlater 

    while True:
        try:
            data = conn.recv(4096).decode()
while True:

        connection, address = my_server.accept()
        print("Successfully Connected")






