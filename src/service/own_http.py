from utils.logger import logger
from utils.common import get_file_name, is_an_image
from constants.constants import VIEWS_URL, HttpResponse


def http_get_handler(request: str) -> str:
    filename = get_file_name(request)
    logger.info("Requested File: " + filename)
    response = ""
    try:
        if is_an_image(filename):
            with open(VIEWS_URL + filename, "rb") as f:
                content = HttpResponse.OK.value.encode() + f.read()
                logger.info(f"Image {filename} sended succesfully")
                return content
        else:
            with open(VIEWS_URL + filename) as f:
                response = HttpResponse.OK.value + f.read()

    except FileNotFoundError:
        logger.error(f"File: {filename} not found")
        response = HttpResponse.NOT_FOUND.value + f"File: {filename} not found"

    except Exception as e:
        logger.error(f"Error Opening File: {e}")
        response = HttpResponse.INTERNAL_SERVER_ERROR.value + str(e)

    logger.info(f"File {filename} sended succesfully")
    return response.encode()
