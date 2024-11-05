#!/usr/bin/env python3
""" A python script that sets up a Basic Flask App."""

from flask import Flask, g, request, render_template
from flask_babel import Babel


class Config:
    """ Default configuration's class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def hello():
    """ Return App's HTML contents """
    return render_template('0-index.html')

# selector function
@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages """
    user = getattr(g, 'user', None)
    if user is not None and hasattr('user', 'locale'):
        return user.locale
    return request.accept_languages(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host='0.0.0.0', degug=True)
