import socket

def run_tcp_client_20_chars():
    # host = '212.182.24.27'
    host = '127.0.0.1'
    port = 2908

    message = input("Podaj wiadomość do wysłania: ")

    formatted_message = message.ljust(20)[:20]

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10.0)

            print(f"Nawiązywanie połączenia z {host}:{port}...")
            s.connect((host, port))
            print("Połączono pomyślnie!\n")

            print(f"Wysyłam (długość {len(formatted_message)}): '{formatted_message}'")
            s.sendall(formatted_message.encode('utf-8'))

            data = s.recv(20)

            if data:
                response = data.decode('utf-8')
                print(f"Otrzymano odpowiedź (długość {len(response)}): '{response}'")
            else:
                print("Serwer zamknął połączenie bez wysłania odpowiedzi.")

    except socket.timeout:
        print("Błąd: Serwer nie odpowiedział w wyznaczonym czasie (Timeout).")
    except ConnectionRefusedError:
        print("Błąd: Serwer odrzucił połączenie. Upewnij się, że serwer działa na tym porcie.")
    except Exception as e:
        print(f"Wystąpił inny błąd sieciowy: {e}")

if __name__ == "__main__":
    run_tcp_client_20_chars()