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


# Selector function
@babel.localeselector
def get_locale():
    """Get the best matched language for response based on user settings,
    or from `Accept-Language` in request headers."""
    # Check if there's a logged-in user with a preferred language
    user = getattr(g, 'user', None)
    if user is not None and hasattr(user, 'locale'):
        return user.locale
    # else if no user defined locale, use browser's preferred language
    return request.accept_languages.best_match(Config.LANGUAGES)


# Selector function
@babel.timezoneselector
def get_timezone():
    """Determines the right timezone of the user,
    otherwise, defaults to application default timezone"""
    # Check if there's a logged-in user with a timezone
    user = getattr(g, 'user', None)
    if user is not None and hasattr(user, 'timezone'):
        return user.timezone
    # else, default to the application's default timezone
    return Config.BABEL_DEFAULT_TIMEZONE


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
