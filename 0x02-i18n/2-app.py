#!/usr/bin/env python3
""" A python script that sets up a Basic Flask App."""

from flask import Flask, render_template, g, request
from flask_babel import Babel


class Config:
    """ Default configuration's class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.configure.from_object(Config)
babel = Babel(app)


# selector function
@babel.timezoneselector
def get_locale():
    """ Determine the best match with our supported languages """
    user = getattr(g, 'user', None)
    if user is not None and hasattr('user', 'locale'):
        return user.locale
    return request.accept_languages(Config.LANGUAGES)
