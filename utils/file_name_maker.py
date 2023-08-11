from os import path, getenv
from .code_gen import generate_code


# Get file name length value
MAX_FILENAME_LENGTH = int(getenv("MAX_FILENAME_LENGTH")) if getenv("MAX_FILENAME_LENGTH") else 6


def get_file_name(original_filename:str):
    filetype = original_filename.split(".")[1]
    while True:
        filename = generate_code(MAX_FILENAME_LENGTH) + f".{filetype}"
        if not path.exists(f"./images/{filename}"):
            break
    return filename