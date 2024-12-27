import re

from utils.logger import logger
from utils.common import get_file_name, is_an_image
from constants.constants import VIEWS_URL, HttpResponse, PUBLIC_URL


def get_response(request: str) -> str:
    headers = request.split("\n")[0]
    logger.info("Request: " + str(headers))
    method = headers.split(" ")[0]
    match method:
        case "GET":
            return get_handler(headers)
        case "POST":
            return post_handler(request)

        case _:
            return HttpResponse.METHOD_NOT_ALLOWED.value.encode()


def post_handler(request: str) -> bytes:
    file_type, file_content = request.split("Content-Type:")[-1].split("\r\n\r\n")
    if "image" not in file_type:
        return HttpResponse.UNSUPPORTED_MEDIA_TYPE.value.encode()

    filename = re.search(r'filename="([^"]+)"', request).group(1)

    try:
        with open(PUBLIC_URL + "/" + filename, "wb") as f:
            f.write(file_content)
    except Exception as e:
        logger.error(f"Error Saving File: {e}")
        return HttpResponse.INTERNAL_SERVER_ERROR.value.encode() + str(e).encode()

    return HttpResponse.OK.value.encode()


def get_handler(headers: str) -> bytes:
    filename = get_file_name(headers)

    if filename == "":
        logger.warning("Empty file requested, returned OK")
        return HttpResponse.OK.value.encode()

    response = ""
    try:
        if is_an_image(filename):
            with open(VIEWS_URL + filename, "rb") as f:
                content = HttpResponse.OK.value.encode() + f.read()
                logger.info(f"200 OK - Image {filename} sended succesfully")
                return content
        else:
            with open(VIEWS_URL + filename) as f:
                response = HttpResponse.OK.value + f.read()

    except FileNotFoundError:
        logger.error(f"404 - File: {filename} not found")
        response = HttpResponse.NOT_FOUND.value + f"File: {filename} not found"

    except Exception as e:
        logger.error(f"Error Opening File: {e}")
        response = HttpResponse.INTERNAL_SERVER_ERROR.value + str(e)

    if filename != "":
        logger.info(f"200 OK - File {filename} sended succesfully")
    return response.encode()
