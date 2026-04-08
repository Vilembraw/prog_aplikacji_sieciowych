import socket

def run_udp_client():
    # host = '212.182.24.27'
    host = '127.0.0.1'
    port = 2901
    message = "Test UDP\n"

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5.0)

        s.sendto(message.encode('utf-8'), (host, port))

        try:
            data, server_address = s.recvfrom(4096)
            print(data.decode('utf-8').strip())
        except socket.timeout:
            print("Czas minął. Serwer UDP nie odpowiedział.")


if __name__ == "__main__":
    run_udp_client()