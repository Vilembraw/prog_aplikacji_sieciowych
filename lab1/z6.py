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

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    try:
        sock.connect((host, port))
        print(f"Successfully connected to {host} on port {port}.")
    except socket.error as e:
        print(f"Connection failed: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()

# python z6.py google.com 80