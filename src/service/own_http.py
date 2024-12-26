from utils.logger import logger
from utils.common import get_file_name, is_an_image
from constants.constants import VIEWS_URL, HttpResponse


def get_response(request: str) -> str:
    headers = request.split("\n")[0]
    logger.info("Request: " + str(headers))
    method = headers.split(" ")[0]
    match method:
        case "GET":
            return http_get_handler(headers)
        case "POST":
            logger.info("POST Handled")
            return HttpResponse.OK.value.encode()
        case _:
            return HttpResponse.METHOD_NOT_ALLOWED.value.encode()


def http_get_handler(headers: str) -> str:
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
