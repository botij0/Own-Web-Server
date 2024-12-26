def get_file_name(headers: str):
    filename = headers.split()[1]

    if filename == "/":
        filename = "/index.html"

    return filename


def is_an_image(filename: str) -> str:
    image_exts = ["ico", "png", "jpg", "jpeg", "webp"]
    extension = filename.split(".")[-1]
    return True if extension in image_exts else False
