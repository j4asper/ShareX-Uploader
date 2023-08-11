from os import getenv
from flask import Request


# Get uploading auth token
TOKEN = getenv("TOKEN")


def authorization_is_valid(request: Request):
    auth_token = request.headers.get("Authorization")
    return auth_token == TOKEN if TOKEN else True