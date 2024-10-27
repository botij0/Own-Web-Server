"""
Simple HTTP/1.0 Server
"""

from utils.common import get_socket
from service.own_http import http_get_handler


def main():
    server_socket = get_socket()
    while True:
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024).decode()

        # Only Supports GET Method
        response = http_get_handler(request)

        client_connection.sendall(response.encode())
        client_connection.close()

    server_socket.close()


if __name__ == "__main__":
    main()
