import socket

hex_data = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"
binary_packet = bytes.fromhex(hex_data.replace(" ", ""))

src_port = int.from_bytes(binary_packet[0:2], byteorder='big')
dst_port = int.from_bytes(binary_packet[2:4], byteorder='big')

payload = binary_packet[8:]
data_str = payload.decode('ascii')

# Format: zad14odp;src;X;dst;Y;data;Z
message = f"zad13odp;src;2900;dst;35211;data;test"
print(f"Wysyłana wiadomość: {message}")

# server_address = ('212.182.24.27', 2910)
server_address = ('127.0.0.1', 2910)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

try:
    sock.sendto(message.encode('ascii'), server_address)
    response, _ = sock.recvfrom(1024)
    print(f"Odpowiedź serwera: {response.decode('ascii')}")
finally:
    sock.close()