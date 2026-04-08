import socket

def get_datetime_from_server():
    host = 'ntp.task.gda.pl'
    port = 13

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.settimeout(5.0)
            s.connect((host, port))
            data = s.recv(1024)

            if data:
                date_time_str = data.decode('ascii').strip()
                print("Aktualna data i czas pobrane z serwera:")
                print(date_time_str)
            else:
                print("Nie otrzymano żadnych danych z serwera.")

    except socket.timeout:
        print(f"Błąd: Przekroczono czas oczekiwania na połączenie z {host}:{port}.")
    except socket.error as e:
        print(f"Błąd sieci lub połączenia: {e}")


if __name__ == "__main__":
    get_datetime_from_server()