import socket
import sys

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <host> <port>")
        sys.exit(1)

    host = sys.argv[1]

    try:
        port = int(sys.argv[2])
    except ValueError:
        print("Error: Port must be an integer.")
        sys.exit(1)

    try:
        service_name = socket.getservbyport(port, 'tcp')
    except OSError:
        service_name = "nieznana"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    try:
        sock.connect((host, port))
        print(f"Port {port} na hoście {host} jest OTWARTY | Usługa: {service_name}")
    except socket.error as e:
        print(f"Port {port} na hoście {host} jest ZAMKNIĘTY | Usługa: {service_name} | Powód: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()

#python z7.py google.com 80