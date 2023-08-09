from flask import Flask, request, send_file
from os import mkdir, path, remove, getenv
from string import ascii_letters, digits
from random import choices


# Create image folder if it doesn't exist
try:
    mkdir("images")
except FileExistsError:
    pass


# Get file name length value
MAX_FILENAME_LENGTH = int(getenv("MAX_FILENAME_LENGTH")) if getenv("MAX_FILENAME_LENGTH") else 6

# Get uploading auth token
TOKEN = getenv("TOKEN")


def generate_filename(length:int):
    return ''.join(choices(ascii_letters + digits, k=length))


def get_file_name(original_filename:str):
    filetype = original_filename.split(".")[1]
    while True:
        filename = generate_filename(MAX_FILENAME_LENGTH) + f".{filetype}"
        if not path.exists(f"./images/{filename}"):
            break
    return filename


def authorization_is_valid(auth_token:str):
    return auth_token == TOKEN if TOKEN else True


app = Flask(__name__)

# Get MAX_UPLOAD_SIZE and set it to MAX_CONTENT_LENGTH for security reasons
app.config["MAX_CONTENT_LENGTH"] = (int(getenv("MAX_UPLOAD_SIZE")) if getenv("MAX_UPLOAD_SIZE") else 10) * 1024 * 1024


@app.route("/", methods=["GET"])
def home():
    return "This is an instance of the ShareX Uploader made by Jasper, you can find the repository here: https://github.com/j4asper/ShareX-Uploader"


##################
#   View Image   #
##################

@app.route("/<image>", methods=["GET"])
def view_image(image):
    if path.exists(f"./images/{image}"):
        return send_file(f"./images/{image}")
    else:
        return "Image not found", 404


##################
#  Upload Image  #
##################

@app.route("/upload", methods=["POST"])
def upload():
    if authorization_is_valid(request.headers.get("Authorization")):
        form = request.form.to_dict()
        filename = get_file_name(form["name"])
        image = request.files.get("image")
        image.save(f"./images/{filename}")
        return f"{filename}", 200
    else:
        return "Not Authorized", 401


if __name__ == "__main__":
    app.run(debug=True)