#!/usr/bin/env python3
import socket
import sys
from time import gmtime, strftime

EXPECTED_A_VER = 4
EXPECTED_A_SRCIP = "212.182.24.27"
EXPECTED_A_DSTIP = "192.168.0.2"
EXPECTED_A_TYPE = 6

EXPECTED_B_SRCPORT = 2900
EXPECTED_B_DSTPORT = 47526
EXPECTED_B_DATA = "network programming is fun"


def check_msgA_syntax(txt):
    parts = txt.split(";")

    if len(parts) != 9:
        return "BAD_SYNTAX"

    if parts[0] != "zad15odpA" or parts[1] != "ver" or parts[3] != "srcip" or parts[5] != "dstip" or parts[7] != "type":
        return "BAD_SYNTAX"

    try:
        ver = int(parts[2])
        srcip = parts[4]
        dstip = parts[6]
        protocol = int(parts[8])

        if ver == EXPECTED_A_VER and srcip == EXPECTED_A_SRCIP and dstip == EXPECTED_A_DSTIP and protocol == EXPECTED_A_TYPE:
            return "TAK"
        else:
            return "NIE"

    except ValueError:
        return "BAD_SYNTAX"


def check_msgB_syntax(txt):
    parts = txt.split(";")

    if len(parts) != 7:
        return "BAD_SYNTAX"

    if parts[0] != "zad15odpB" or parts[1] != "srcport" or parts[3] != "dstport" or parts[5] != "data":
        return "BAD_SYNTAX"

    try:
        srcport = int(parts[2])
        dstport = int(parts[4])
        data_content = parts[6]

        if srcport == EXPECTED_B_SRCPORT and dstport == EXPECTED_B_DSTPORT and data_content == EXPECTED_B_DATA:
            return "TAK"
        else:
            return "NIE"

    except ValueError:
        return "BAD_SYNTAX"


def run_server(host='127.0.0.1', port=2911):
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
            data_str = data_raw.decode('utf-8', errors='ignore').strip()

            log_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            print(f"[{log_time}] Otrzymano od {address}: {data_str}")

            if data_raw:
                parts = data_str.split(";")

                if parts[0] == "zad15odpA":
                    answer_str = check_msgA_syntax(data_str)
                elif parts[0] == "zad15odpB":
                    answer_str = check_msgB_syntax(data_str)
                else:
                    answer_str = "BAD_SYNTAX"

                sock.sendto(answer_str.encode('utf-8'), address)
                print(f"[{log_time}] Odesłano: {answer_str}")

    except KeyboardInterrupt:
        print("\nZamykanie serwera...")
    finally:
        sock.close()


if __name__ == "__main__":
    run_server()