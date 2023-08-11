from os import path, getenv
import sqlite3
from .code_gen import generate_code
from flask import Request


if not path.exists(f"./short_urls.db"):
    with sqlite3.connect("./short_urls.db") as con:
        cur = con.cursor()
        cur.execute("CREATE TABLE url(original, short)")


SHORT_URL_LENGTH = int(getenv("SHORT_URL_LENGTH")) if getenv("SHORT_URL_LENGTH") else 4


def shorten(request: Request):
    original_url = request.form.get("url")
    
    # Check if URL already exists in database
    with sqlite3.connect("./short_urls.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM url WHERE original = ?", (original_url,))
        res = cur.fetchall()
        if res:
            return res[0][1]
    
    while True:
        code = generate_code(SHORT_URL_LENGTH)
        with sqlite3.connect("./short_urls.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM url WHERE short = ?", (code,))
            if not cur.fetchall():
                cur.execute("INSERT INTO url (original, short) VALUES(?, ?)", (original_url, code,))
                break

    return code


def get_original_url(code):
    with sqlite3.connect("./short_urls.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM url WHERE short = ?", (code,))
        res = cur.fetchall()
        if res:
            return res[0][0]
        else:
            return None