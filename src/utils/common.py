def get_file_name(headers: str):
    filename = headers.split()[1]

    if filename == "/":
        filename = "/index.html"

    return filename


def get_content_lenght(request: bytes) -> int:
    if request.find(b"Content-Length:") != -1:
        return int(request.split(b"Content-Length:")[-1].split(b"\r\n")[0].strip())
    else:
        return 0


def is_an_image(filename: str) -> str:
    image_exts = ["ico", "png", "jpg", "jpeg", "webp"]
    extension = filename.split(".")[-1]
    return True if extension in image_exts else False
