#!/usr/bin/env python3
import socket
import sys
from time import gmtime, strftime

EXPECTED_SRC = 60788
EXPECTED_DST = 2901
EXPECTED_DATA = "programming in python is fun"


def check_msg_syntax(txt):
    parts = txt.split(";")

    if len(parts) != 7:
        return "BAD_SYNTAX"

    if parts[0] != "zad13odp" or parts[1] != "src" or parts[3] != "dst" or parts[5] != "data":
        return "BAD_SYNTAX"

    try:
        src_port = int(parts[2])
        dst_port = int(parts[4])
        data_content = parts[6]

        if src_port == EXPECTED_SRC and dst_port == EXPECTED_DST and data_content == EXPECTED_DATA:
            return "TAK"
        else:
            return "NIE"

    except ValueError:
        return "BAD_SYNTAX"


def run_server(host='127.0.0.1', port=2910):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.bind((host, port))
    except socket.error as e:
        print(f"Błąd bindowania gniazda: {e}")
        sys.exit(1)

    print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] Serwer UDP nasłuchuje na {host}:{port}...")

    try:
        while True:
            data_raw, address = sock.recvfrom(1024)
            data_str = data_raw.decode('ascii', errors='ignore').strip()

            log_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            print(f"[{log_time}] Otrzymano wiadomość od {address}: {data_str}")

            if data_raw:
                answer_str = check_msg_syntax(data_str)
                sock.sendto(answer_str.encode('ascii'), address)
                print(f"[{log_time}] Odesłano odpowiedź: {answer_str}")

    except KeyboardInterrupt:
        print("\nZamykanie serwera...")
    finally:
        sock.close()


if __name__ == "__main__":
    run_server()