#!/usr/bin/env python3
import socket
import time

IP = '127.0.0.1'
PORT_TCP = 5001
PORT_UDP = 5002
COUNT = 100
DATA = b"x" * 1024

def test_tcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT_TCP))
    start = time.time()
    for _ in range(COUNT):
        s.sendall(DATA)
    s.recv(1024)
    end = time.time()
    s.close()
    return end - start

def test_udp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((IP, 5003))
    s.settimeout(3.0)
    start = time.time()
    for _ in range(COUNT):
        s.sendto(DATA, (IP, PORT_UDP))
    s.recvfrom(1024)
    end = time.time()
    s.close()
    return end - start

if __name__ == "__main__":
    print(f"TCP: {test_tcp():.4f}s")
    print(f"UDP: {test_udp():.4f}s")