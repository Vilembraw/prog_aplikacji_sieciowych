import socket
import sys

def recvall(sock, msgLen):
    msg = b""
    bytesRcvd = 0
    while bytesRcvd < msgLen:
        chunk = sock.recv(msgLen - bytesRcvd)
        if not chunk:
            break
        bytesRcvd += len(chunk)
        msg += chunk
    return msg

remoteServerIP = "212.182.24.27"
port = 22

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP, port))

    if result == 0:
        sock.sendall(b'Just a text \n')
        received_data = recvall(sock, 4096)
        print(f"Port {port} is open, data = {received_data}")
    else:
        print(f"Port {port} is closed")

    sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()