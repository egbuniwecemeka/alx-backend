#!/usr/bin/env python3
""" A python script that parametrizes templates based on translations """

from flask import Flask, render_template
from flask_babel import gettext as _, Babel, request


class Config:
    """ Default configuration class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.congig.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def hello():
    """ returns the welcome messaage with translations """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ Gets the requested language set in URL parameter. """
    user = getattr(g, 'user', None)

    if user is not None and hasattr('user', 'locale'):
        return user.locale 
    return request.args.get('lang', 'en')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)