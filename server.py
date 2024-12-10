import socket
from _thread import *

server = ""
port = 4424

my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    my_server.bind((server, port))
except socket.error as e:
    print(str(e))

# Refers to how many players can connect to the server at once
my_server.listen(2)
print("Waiting for a connection...")


def threaded(connection, player):
    connection.send(str.encode('Connected'))  # DewItlater
    reply = ''
    while True:
        try:
            data = connection.recv(2048).decode()
            reply = data.decode('utf-8')
            if not data:
                print('Disconnected')
                break
            else:
                print('Received : ', reply)
                print('Sending : ', reply)
            connection.sendall(str.encode(reply))
        except:
            break
    print('Lost Connection')
    connection.close()


while True:

    connection, address = my_server.accept()
    print("Successfully Connected to", address)
    start_new_thread(threaded, (connection,))
