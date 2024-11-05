#!/usr/bin/env python3
""" A python script thats sets up a basic Flask App """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Returns application Welcome Message """
    return render_template('0-index.html')


if __name__ == "__main__":
     app.run(host = "0.0.0.0", debug=True)