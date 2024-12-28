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
    METHOD_NOT_ALLOWED = (
        "HTTP/1.0 405 Method Not Allowed\r\n"
        "Content-Type: text/html\r\n"
        "Connection: close\r\n"
        "\r\n"
        "<html>"
        "<head><title>Method Not Allowed</title></head>"
        "<body><h1>Error 405: Method Not Allowed</h1>"
        "</body></html>"
    )
    NOT_FOUND_BASIC = "HTTP/1.0 404 Not Found\n\n"
    NOT_FOUND = (
        "HTTP/1.1 404 Not Found\r\n"
        "Content-Type: text/html\r\n"
        "Connection: close\r\n"
        "\r\n"
        "<html>"
        "<head><title>Resource Not Found</title></head>"
        "<body><h1>Error 404: Not Found</h1>"
        "<p>The resource you have requested has not been found</p>"
        "</body></html>"
    )
    UNSUPPORTED_MEDIA_TYPE = (
        "HTTP/1.1 415 Unsupported Media Type\r\n"
        "Content-Type: text/html\r\n"
        "Connection: close\r\n"
        "\r\n"
        "<html>"
        "<head><title>Unsupported Media Type</title></head>"
        "<body><h1>Error 415: Unsupported Media Type</h1>"
        "<p>Only JPG images are supported. Please upload a valid file.</p>"
        "<br /><br />"
        "<a href='form.html'>Go Back To Form</a>"
        "</body></html>"
    )

    # Server Error
    INTERNAL_SERVER_ERROR = "HTTP/1.0 500 Internal Server Error\n\n"
    (
        "HTTP/1.0 500 Internal Server Error\r\n"
        "Content-Type: text/html\r\n"
        "Connection: close\r\n"
        "\r\n"
        "<html>"
        "<head><title>Internal Server Error</title></head>"
        "<body><h1>Error 500: Internal Server Error</h1>"
        "<p>Please try again later.</p>"
        "</body></html>"
    )
