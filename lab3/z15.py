import socket

hex_string = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e"
hex_data = hex_string.replace(" ", "")
packet = bytes.fromhex(hex_data)

version = packet[0] >> 4
ihl = (packet[0] & 0x0F) * 4

protocol = packet[9]

src_ip = f"{packet[12]}.{packet[13]}.{packet[14]}.{packet[15]}"
dst_ip = f"{packet[16]}.{packet[17]}.{packet[18]}.{packet[19]}"

msg_a = f"zad15odpA;ver;{version};srcip;{src_ip};dstip;{dst_ip};type;{protocol}"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5.0)
server_address = ('127.0.0.1', 2911)

try:
    sock.sendto(msg_a.encode('utf-8'), server_address)
    response_a, _ = sock.recvfrom(1024)
    resp_a_text = response_a.decode('utf-8')
    print(f"Serwer (Msg A): {resp_a_text}")

    if resp_a_text == "TAK" and protocol == 6:
        tcp_start = ihl

        src_port = int.from_bytes(packet[tcp_start:tcp_start + 2], byteorder='big')
        dst_port = int.from_bytes(packet[tcp_start + 2:tcp_start + 4], byteorder='big')

        data_offset = (packet[tcp_start + 12] >> 4) * 4
        data_start = tcp_start + data_offset

        data = packet[data_start:].decode('utf-8')

        msg_b = f"zad15odpB;srcport;{src_port};dstport;{dst_port};data;{data}"

        sock.sendto(msg_b.encode('utf-8'), server_address)
        response_b, _ = sock.recvfrom(1024)
        print(f"Serwer (Msg B): {response_b.decode('utf-8')}")

except socket.timeout:
    print("Brak odpowiedzi od serwera (timeout)")
finally:
    sock.close()