import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 55555))
message = s.recv(1024) #how many bits i wanna recieve
s.close()

print(message.decode())