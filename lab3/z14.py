import socket

hex_string = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"
hex_data = hex_string.replace(" ", "")
segment = bytes.fromhex(hex_data)

src_port = int.from_bytes(segment[0:2], byteorder='big')
dst_port = int.from_bytes(segment[2:4], byteorder='big')

data_offset = (segment[12] >> 4) * 4
data = segment[data_offset:].decode('utf-8')

message = f"zad13odp;src;{src_port};dst;{dst_port};data;{data}"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5.0)
# server_address = ('212.182.24.27', 2909)
server_address = ('127.0.0.1', 2910)


try:
    sock.sendto(message.encode('utf-8'), server_address)
    response, _ = sock.recvfrom(1024)
    print(response.decode('utf-8'))
except socket.timeout:
    print("Brak odpowiedzi od serwera (timeout)")
finally:
    sock.close()