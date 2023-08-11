from flask import Flask, request, send_file, redirect
from os import mkdir, path, getenv
from utils import authorization_is_valid, upload_image, shorten, get_original_url


# Create image folder if it doesn't exist
try:
    mkdir("images")
except FileExistsError:
    pass


app = Flask(__name__)

# Get MAX_UPLOAD_SIZE and set it to MAX_CONTENT_LENGTH for security reasons
app.config["MAX_CONTENT_LENGTH"] = (int(getenv("MAX_UPLOAD_SIZE")) if getenv("MAX_UPLOAD_SIZE") else 10) * 1024 * 1024



@app.route("/", methods=["GET"])
def home():
    return "This is an instance of the ShareX Uploader made by Jasper, you can find the repository here: https://github.com/j4asper/ShareX-Uploader"



##################
#   View Image   #
##################

@app.route("/<text>", methods=["GET"])
def get_file_or_short_url(text):
    if "." in text:
        if path.exists(f"./images/{text}"):
            return send_file(f"./images/{text}")
        else:
            return "Image not found", 404
        
    else:
        original_url = get_original_url(text)
        if original_url:
            return redirect(original_url)
        else:
            return "Short URL not found", 404



##################
#  Upload Image  #
##################

@app.route("/upload", methods=["POST"])
def upload():
    if authorization_is_valid(request):
        filename = upload_image(request)
        return filename, 200
    else:
        return "Not Authorized", 401



###################
#  URL Shortener  #
###################

@app.route("/shorten", methods=["POST"])
def shorten_url():
    if authorization_is_valid(request):
        short_url_code = shorten(request)
        return short_url_code, 200
    else:
        return "Not Authorized", 401


if __name__ == "__main__":
    app.run(debug=True)