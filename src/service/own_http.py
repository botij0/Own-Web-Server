import os

from utils.logger import logger
from utils.common import get_file_name, is_an_image
from constants.constants import VIEWS_URL, HttpResponse, PUBLIC_URL


def get_response(request: bytes) -> bytes:
    headers = request.decode("utf-8", errors="replace").split("\n")[0]
    if len(headers) < 0:
        return b""
    logger.info("Request: " + str(headers))
    method = headers.split(" ")[0]
    match method:
        case "GET":
            return get_handler(headers)
        case "POST":
            return post_handler(request)
        case "DELETE":
            return delete_handler(headers)

        case _:
            return HttpResponse.METHOD_NOT_ALLOWED.value.encode()


def delete_handler(headers: str) -> bytes:
    filename = get_file_name(headers)
    try:
        os.remove(PUBLIC_URL + filename)
        logger.info(f"200 OK - file {filename} deleted succesfully")
        return HttpResponse.OK.value.encode()

    except FileNotFoundError:
        logger.error(f"404 NOT FOUND - File: {filename} not found")
        return HttpResponse.NOT_FOUND.value.encode()

    except Exception as e:
        logger.error(f"Error deleting {filename}: {e}")
        return HttpResponse.INTERNAL_SERVER_ERROR.value.encode() + str(e).encode()


def post_handler(request: bytes) -> bytes:
    file_type, file_content = request.split(b"Content-Type:")[-1].split(b"\r\n\r\n")
    if b"image/jpeg" != file_type.strip():
        logger.error("415 Unsupported Media Type - Image is'nt a JPG")
        return HttpResponse.UNSUPPORTED_MEDIA_TYPE.value.encode()

    try:
        with open(PUBLIC_URL + "/main.jpg", "wb") as f:
            f.write(file_content)
    except Exception as e:
        logger.error(f"Error Saving File: {e}")
        return HttpResponse.INTERNAL_SERVER_ERROR.value.encode() + str(e).encode()

    logger.info("201 CREATED - Image saved")

    try:
        with open(VIEWS_URL + "/index.html", "rb") as f:
            return HttpResponse.CREATED.value.encode() + f.read()

    except Exception as e:
        logger.error(f"Error redirecting to index.html: {e}")
        return HttpResponse.INTERNAL_SERVER_ERROR.value.encode() + str(e).encode()


def get_handler(headers: str) -> bytes:
    filename = get_file_name(headers)

    if filename == "":
        logger.warning("Empty file requested, returned OK")
        return HttpResponse.OK.value.encode()

    try:
        if is_an_image(filename):
            with open(PUBLIC_URL + filename, "rb") as f:
                content = HttpResponse.OK.value.encode() + f.read()
                logger.info(f"200 OK - Image {filename} sended succesfully")
                return content
        else:
            with open(VIEWS_URL + filename) as f:
                content = HttpResponse.OK.value + f.read()
                logger.info(f"200 OK - File {filename} sended succesfully")
                return content.encode()
    except FileNotFoundError:
        logger.error(f"404 NOT FOUND - File: {filename} not found")
        return HttpResponse.NOT_FOUND.value.encode()

    except Exception as e:
        logger.error(f"Error Opening File: {e}")
        return HttpResponse.INTERNAL_SERVER_ERROR.value.encode() + str(e).encode()
