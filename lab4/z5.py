import socket

HOST = '127.0.0.1'
PORT = 2916

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

while True:
    data, client_address = server_socket.recvfrom(1024)
    if data:
        ip_address = data.decode('utf-8').strip()
        try:
            hostname, _, _ = socket.gethostbyaddr(ip_address)
            response = hostname
        except socket.herror:
            response = "Nie znaleziono nazwy hosta"
        except Exception:
            response = "Błędny adres IP"

        server_socket.sendto(response.encode('utf-8'), client_address)