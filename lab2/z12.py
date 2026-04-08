import socket


def send_all_fixed(sock, message_bytes):
    total_sent = 0
    while total_sent < len(message_bytes):
        sent = sock.send(message_bytes[total_sent:])
        if sent == 0:
            raise RuntimeError("Połączenie przerwane podczas wysyłania")
        total_sent += sent
    return total_sent


def recv_all_fixed(sock, n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data


def run_tcp_client_safe():
    # host = '212.182.24.27'
    host = '127.0.0.1'
    port = 2908
    REQUIRED_LENGTH = 20

    message = input(f"Podaj wiadomość (zostanie sformatowana do {REQUIRED_LENGTH} znaków): ")
    formatted_message = message.ljust(REQUIRED_LENGTH)[:REQUIRED_LENGTH]
    message_bytes = formatted_message.encode('utf-8')

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10.0)
            s.connect((host, port))

            print(f"Wysyłanie: '{formatted_message}'...")
            send_all_fixed(s, message_bytes)

            print("Oczekiwanie na pełną odpowiedź (20 bajtów)...")
            response_bytes = recv_all_fixed(s, REQUIRED_LENGTH)

            if response_bytes:
                print(f"Odebrano: '{response_bytes.decode('utf-8')}'")
            else:
                print("Błąd: Połączenie zamknięte przed odebraniem kompletu danych.")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    run_tcp_client_safe()