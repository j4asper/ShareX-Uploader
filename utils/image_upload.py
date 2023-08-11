from flask import Request
from .file_name_maker import get_file_name


def upload_image(request: Request):
    form = request.form.to_dict()
    filename = get_file_name(form["name"])
    image = request.files.get("image")
    image.save(f"./images/{filename}")
    return filename