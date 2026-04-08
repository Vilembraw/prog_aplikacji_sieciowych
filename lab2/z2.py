import socket

def run_tcp_client():
    # host = '212.182.24.27'
    host = '127.0.0.1'
    port = 2900

    message = "Test\n"

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10.0)

            print(f"Nawiązywanie połączenia z {host}:{port}...")
            s.connect((host, port))
            print("Połączono pomyślnie!\n")

            print(f"Wysyłam: {message.strip()}")
            s.sendall(message.encode('utf-8'))

            data = s.recv(1024)

            if data:
                response = data.decode('utf-8').strip()
                print(f"Otrzymano odpowiedź: {response}")
            else:
                print("Serwer zamknął połączenie bez wysłania odpowiedzi.")

    except socket.timeout:
        print("Błąd: Serwer nie odpowiedział w wyznaczonym czasie (Timeout).")
    except ConnectionRefusedError:
        print("Błąd: Serwer odrzucił połączenie. Upewnij się, że serwer działa na tym porcie.")
    except Exception as e:
        print(f"Wystąpił inny błąd sieciowy: {e}")


if __name__ == "__main__":
    run_tcp_client()