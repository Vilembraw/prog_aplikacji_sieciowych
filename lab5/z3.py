#!/usr/bin/env python3
import socket
import sys

HOST = '212.182.24.27'
TCP_PORT = 2913
UDP_MSG = b"PING"
EXPECTED_TCP_RESP = "Congratulations! You found the hidden"


def find_udp_sequence():
    sequence = []
    for port in range(1, 65536):
        if str(port).endswith("666"):
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_sock:
                udp_sock.settimeout(0.5)
                try:
                    udp_sock.sendto(UDP_MSG, (HOST, port))
                    data, _ = udp_sock.recvfrom(1024)
                    if data.decode('utf-8') == "PONG":
                        sequence.append(port)
                except socket.timeout:
                    continue
    return sequence


def knock(sequence):
    for port in sequence:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_sock:
            udp_sock.sendto(UDP_MSG, (HOST, port))


def connect_tcp():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_sock:
        tcp_sock.settimeout(2.0)
        try:
            tcp_sock.connect((HOST, TCP_PORT))
            data = tcp_sock.recv(1024)
            print(data.decode('utf-8'))
        except socket.error as e:
            print(f"TCP Connection failed: {e}")


def run():
    print("Scanning for UDP ports ending in 666...")
    sequence = find_udp_sequence()
    if not sequence:
        print("No sequence found.")
        return

    print(f"Found sequence: {sequence}. Knocking...")
    knock(sequence)

    print(f"Connecting to TCP {TCP_PORT}...")
    connect_tcp()


if __name__ == "__main__":
    run()