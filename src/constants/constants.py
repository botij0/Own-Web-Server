from enum import Enum

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000
VIEWS_URL = "src/views"
PUBLIC_URL = "src/public"


class HttpResponse(Enum):
    # Satisfactory Responses
    OK = "HTTP/1.0 200 OK\n\n"
    CREATED = "HTTP/1.0 201 Created\n\n"

    # Client Error
    METHOD_NOT_ALLOWED = "HTTP/1.0 405 Method Not Allowed\n\n"
    NOT_FOUND = "HTTP/1.0 404 Not Found\n\n"
    UNSUPPORTED_MEDIA_TYPE = "HTTP/1.0 415 Unsupported Media Type"

    # Server Error
    INTERNAL_SERVER_ERROR = "HTTP/1.0 500 Internal Server Error\n\n"
