import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 2912

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()
    try:
        data = client_socket.recv(1024)
        if data:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            client_socket.sendall(now.encode('utf-8'))
    finally:
        client_socket.close()