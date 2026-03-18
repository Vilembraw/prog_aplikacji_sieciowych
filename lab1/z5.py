import sys
import socket

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <host>")
        sys.exit(1)

    ip_address = sys.argv[1]

    try:
        result = socket.gethostbyaddr(ip_address)
        hostname = result[0]
        print(f"Found hostname: {hostname}")

    except socket.herror:
        print("Unkown hostname")
    except socket.gaierror:
        print("Unkown ip")
    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    main()

# python z5.py 1.1.1.1