import socket 
# (end points)socket : lower level of connected (in python)

# Creat a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
# SOCK_DGRAM : UDP,    SOCK_STREAM : TCP

s.bind(('127.0.0.1', 55555))
s.listen()

while True:
    client, address = s.accept() 
    #accept is method we use, when a client tries to connect to the server or socket and we accept it
    # we accpet every single client

    print("Connected to {}".format(address))
    client.send("You are connected!".encode())
    client.close()
