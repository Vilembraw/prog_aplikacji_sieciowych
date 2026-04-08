import socket
import re

HOST = '127.0.0.1'
PORT = 2915

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

while True:
    data, client_address = server_socket.recvfrom(1024)
    if data:
        try:
            expression = data.decode('utf-8').strip()
            match = re.match(r'^\s*(-?\d+(?:\.\d+)?)\s*([\+\-\*\/])\s*(-?\d+(?:\.\d+)?)\s*$', expression)

            if match:
                num1 = float(match.group(1))
                op = match.group(2)
                num2 = float(match.group(3))

                if op == '+':
                    result = num1 + num2
                elif op == '-':
                    result = num1 - num2
                elif op == '*':
                    result = num1 * num2
                elif op == '/':
                    result = num1 / num2 if num2 != 0 else "Błąd: Dzielenie przez zero"

                response = str(result)
            else:
                response = "Błąd formatu. Użyj formatu: liczba operator liczba (np. 5 + 3)"

        except Exception:
            response = "Wystąpił błąd podczas przetwarzania"

        server_socket.sendto(response.encode('utf-8'), client_address)