from enum import Enum

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000
VIEWS_URL = "src/views"


class HttpResponse(Enum):
    OK = "HTTP/1.0 200 OK\n\n"
    NOT_FOUND = "HTTP/1.0 404 Not Found\n\n"
    INTERNAL_SERVER_ERROR = "HTTP/1.0 500 Internal Server Error\n\n"
