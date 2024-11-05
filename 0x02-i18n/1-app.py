#!/usr/bin/env python3
""" A python script thats sets up and instantiates a basic Flask App"""

from flask import Flask, render_template, g, request
from flask_babel import Babel


class Config:
    """ Configures available languages for the application """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def hello():
    """ Returns the welcome message for my application """
    return render_template('0-index.html')


@babel.localeselector
def get_locale():
    """Get the best matched language based on user settings or request headers."""
    # use locale from user settings, if user is logged in
    user = getattr(g, 'user', None)
    if user is not None and hasattr(user, 'locale'):
        return user.locale
    # else guess the language from the user accept
    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone():
    """Get the timezone of the user, otherwise """
    user = getattr(g, 'user', None)
    if user is not None and hasattr(user, 'timezone'):
        return user.timezone
    #
    return Config.BABEL_DEFAULT_TIMEZONE


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
