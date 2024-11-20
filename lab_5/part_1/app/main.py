# https://cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service

import datetime

from flask import Flask, render_template
from mark_text import mark_text

app = Flask(__name__)

# bucket:
# still-entity-437215-t9-bucket
# TODO fetch from cloud storage
input_file_path = ''


@app.route("/")
def root():
    mark_text() # TODO modify to save to cloud storage instead of locally
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)