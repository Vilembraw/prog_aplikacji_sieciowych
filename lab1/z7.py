import socket
import sys

def scan_ports():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <target>")
        sys.exit(1)

    target = sys.argv[1]

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Error: Hostname could not be resolved.")
        sys.exit(1)

    try:
        print("Scanning ports...")
        for port in range(1, 1000):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((target_ip, port))

            if result == 0:
                print(f"Port {port}: OPEN")

            sock.close()

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()




if __name__ == "__main__":
    scan_ports()

# python z7.py google.com