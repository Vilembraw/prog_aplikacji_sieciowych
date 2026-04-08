import socket


def run_udp_calculator_client():
    # host = '212.182.24.27'
    host = '127.0.0.1'
    port = 2902

    liczba1 = input("Podaj pierwszą liczbę: ")
    operator = input("Podaj operator (+, -, *, /): ")
    liczba2 = input("Podaj drugą liczbę: ")

    message = f"{liczba1} {operator} {liczba2}"

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5.0)

        s.sendto(message.encode('utf-8'), (host, port))

        try:
            data, _ = s.recvfrom(4096)
            print("Odpowiedź serwera:", data.decode('utf-8').strip())
        except socket.timeout:
            print("Brak odpowiedzi od serwera (timeout).")


if __name__ == "__main__":
    run_udp_calculator_client()