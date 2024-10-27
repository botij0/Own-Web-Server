"""
Simple HTTP/1.0 Server
"""

import socket

from utils.logger import logger

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000


def main():
    # Creates new socket: AF_INET -> IPv4; SOCK_STREAM -> TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Config Socket Level: SOL_SOCKET -> self Socket; SO_REUSEADDR -> reuse addr if reset; 1 -> True
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Associate socket to add and port
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    # Listen incoming conns: 1 -> size of the buffer.
    server_socket.listen(1)
    logger.info(f"Listening on port...{SERVER_PORT}")

    while True:
        client_connection, client_address = server_socket.accept()

        request = client_connection.recv(1024).decode()
        logger.info(request)

        # Read a File
        file = open("src/views/index.html")
        content = file.read()
        file.close()

        response = "HTTP/1.0 200 OK\n\n" + content
        client_connection.sendall(response.encode())
        client_connection.close()

    server_socket.close()


if __name__ == "__main__":
    main()
