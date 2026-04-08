#!/usr/bin/env python3
import socket
import sys

HOST = '212.182.24.27'
PORT = 2912


def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOST, PORT))
        print(f"Połączono z serwerem {HOST}:{PORT}. Rozpocznij zgadywanie!")
    except socket.error as e:
        print(f"Nie udało się połączyć z serwerem: {e}")
        sys.exit(1)

    try:
        while True:
            user_input = input("Podaj liczbę (lub 'q' aby wyjść): ").strip()

            if user_input.lower() == 'q':
                print("Zamykanie klienta...")
                break

            if not user_input.isdigit():
                print("Błąd: Wpisana wartość musi być liczbą całkowitą.")
                continue


            message = user_input

            sock.sendall(message.encode('utf-8'))

            response = sock.recv(1024)
            if not response:
                print("Serwer zamknął połączenie.")
                break

            print(f"Odpowiedź serwera: {response.decode('utf-8', errors='ignore').strip()}")

    except KeyboardInterrupt:
        print("\nPrzerwano działanie programu (Ctrl+C).")
    finally:
        sock.close()


if __name__ == "__main__":
    run_client()