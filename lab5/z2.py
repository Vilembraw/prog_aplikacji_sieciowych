#!/usr/bin/env python3
import socket
import sys
import random

HOST = '127.0.0.1'
PORT = 2912


def run_server():
    sekretna_liczba = random.randint(1, 5)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        sock.bind((HOST, PORT))
        sock.listen(1)
    except socket.error:
        sys.exit(1)

    conn, addr = sock.accept()

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            wiadomosc = data.decode('utf-8').strip()

            if not wiadomosc.isdigit():
                odpowiedz = "ERROR: NOT A NUMBER"
            else:
                liczba_klienta = int(wiadomosc)

                if liczba_klienta < sekretna_liczba:
                    odpowiedz = "MNIEJSZA"
                elif liczba_klienta > sekretna_liczba:
                    odpowiedz = "WIEKSZA"
                else:
                    odpowiedz = "ROWNA"
                    conn.sendall(odpowiedz.encode('utf-8'))
                    break

            conn.sendall(odpowiedz.encode('utf-8'))

    sock.close()


if __name__ == "__main__":
    run_server()