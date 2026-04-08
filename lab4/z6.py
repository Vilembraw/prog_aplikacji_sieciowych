import socket

HOST = '127.0.0.1'
PORT = 2917

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

while True:
    data, client_address = server_socket.recvfrom(1024)
    if data:
        hostname = data.decode('utf-8').strip()
        try:
            ip_address = socket.gethostbyname(hostname)
            response = ip_address
        except socket.gaierror:
            response = "Nie znaleziono adresu IP dla podanej nazwy"
        except Exception:
            response = "Wystąpił błąd"

        server_socket.sendto(response.encode('utf-8'), client_address)