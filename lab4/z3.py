import socket

HOST = '127.0.0.1'
PORT = 2914

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

while True:
    data, client_address = server_socket.recvfrom(1024)
    if data:
        server_socket.sendto(data, client_address)