#!/usr/bin/env python3
import socket
import threading

IP = '127.0.0.1'
PORT_TCP = 5001
PORT_UDP = 5002
COUNT = 100

def handle_tcp():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((IP, PORT_TCP))
        s.listen(1)
        conn, _ = s.accept()
        with conn:
            for _ in range(COUNT):
                conn.recv(1024)
            conn.sendall(b"DONE")

def handle_udp():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((IP, PORT_UDP))
        s.settimeout(3.0)
        for _ in range(COUNT):
            s.recvfrom(1024)
        s.sendto(b"DONE", (IP, 5003))

if __name__ == "__main__":
    threading.Thread(target=handle_tcp).start()
    handle_udp()