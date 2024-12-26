"""
Simple HTTP/1.0 Server
"""

import socket

from utils.logger import logger
from constants.constants import SERVER_HOST, SERVER_PORT
from service.own_http import get_response


def main():
    server_socket = get_socket()
    while True:
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024).decode("utf-8", errors="replace")

        # Only Supports GET Method

        response = get_response(request)

        client_connection.sendall(response)
        client_connection.close()

    server_socket.close()


def get_socket() -> socket:
    # Creates new socket: AF_INET -> IPv4; SOCK_STREAM -> TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Config Socket Level: SOL_SOCKET -> self Socket; SO_REUSEADDR -> reuse addr if reset; 1 -> True
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Associate socket to add and port
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    # Listen incoming conns: 1 -> size of the buffer.
    server_socket.listen(1)
    logger.info(f"Listening on port...{SERVER_PORT}")

    return server_socket


if __name__ == "__main__":
    main()
