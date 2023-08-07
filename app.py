from flask import Flask, request, send_file
from os import mkdir, path, remove, getenv
from secrets import token_urlsafe


# Create image folder if it doesn't exist
try:
    mkdir("images")
except FileExistsError:
    pass


def generate_file_name(original_filename:str):
    filetype = original_filename.split(".")[1]
    while True:
        filename = token_urlsafe(8) + f".{filetype}"
        if not path.exists(f"./images/{filename}"):
            break
    return filename


def authorization_is_valid(token:str):
    system_token = getenv("TOKEN")
    if system_token:
        return token == getenv("TOKEN")
    else:
        return True


app = Flask(__name__)


@app.route("/<image>", methods=["GET"])
def view_image(image):
    if path.exists(f"./images/{image}"):
        return send_file(f"./images/{image}")
    else:
        return "Image not found", 404


@app.route("/upload", methods=["POST"])
def upload():
    if authorization_is_valid(request.headers.get("Authorization")):
        form = request.form.to_dict()
        filename = generate_file_name(form["name"])
        image = request.files.get("image")
        image.save(f"./images/{filename}")
        return f"{filename}", 200
    else:
        return "Not Authorized", 401


if __name__ == "__main__":
    app.run(debug=True)