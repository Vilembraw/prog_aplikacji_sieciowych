import socket

def run_tcp_client():
    # host = '212.182.24.27'
    host = '127.0.0.1'
    port = 2900

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        while True:
            message = input()

            if message.lower() in ['exit', 'quit']:
                break

            message_to_send = message + '\n'
            s.sendall(message_to_send.encode('utf-8'))

            data = s.recv(4096)
            if not data:
                break

            print(data.decode('utf-8').strip())


if __name__ == "__main__":
    run_tcp_client()