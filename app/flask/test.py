


import sys

from flask import Flask, render_template, request, json
from db import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/get_wav", methods=["POST"])
def get_wav():

    input_voice = str(json.loads(request.values.get("voice")))
































































    if __name__ == '__main__':
        app.run(debug=True)
