#!/usr/bin/env python3
""" A python script that parametrizes templates based on translations """

from flask import Flask, render_template
from jinja2 import Environment, FileSystemLoader
from flask_babel import gettext as _, Babel, request

# Set up Jinja2 environment
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=True  # Enable autoescape for security
)

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)


@app.route("/", strict_slashes=False)
def hello():
    """ returns the welcome messaage with translations """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """ Gets the requested language set in URL parameter. """
    return request.args.get('lang', 'en')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
