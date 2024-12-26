import socket

from utils.logger import logger
from constants.constants import SERVER_HOST, SERVER_PORT


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


def get_file_name(request: str):
    headers = request.split("\n")
    if len(headers) < 2:
        return ""
    logger.info("Method: " + str(headers[0]))
    filename = headers[0].split()[1]

    if filename == "/":
        filename = "/index.html"

    return filename


def is_an_image(filename: str) -> str:
    image_exts = ["ico", "png", "jpg", "jpeg", "webp"]
    extension = filename.split(".")[-1]
    return True if extension in image_exts else False
