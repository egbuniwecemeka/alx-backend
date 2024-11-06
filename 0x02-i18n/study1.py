#!/usr/bin/env python3
""" A pthon script that configures an application and creates an Instance of it """

from flask import Flask
from flask_babel import Babel


app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

# To disable jinja include configure_jinja=False
babel = Babel(app)

""" CONFIGURATION VALUES THAT CAN BE USED TO CHANGE BABEL'S INTERNAL DEFAULTS

        BABEL_DEFAULT_LOCALE - Language to use. Default is 'en'
        BABEL_DEFAULT_TIMEZONE - Timezone to use. Defaults to UTC which apps use internally
        BABEL_TRANSLATION_DIRECTORIES - semi-colon seperated absolute/relative paths to translation folders/directories. Default is translations
        BABEL_DOMAIN - Message domain used by the application

        Selector fuctions will be handy when you have to have multiple applications for different users.

        localeselector() - Called the first time the babel extension needs the locale (language code) of the current user
        timezoneselector() - called the first time the timezone of the current user is needed
        Example code: 1-app.py and 2-app.py

        Note: To switch a language between a request, refresh() the cache

        USING TRANSLATIONS: There are two fuctions responsible for translation namely:
        - gettext() - Translates singular strings
        - ngettext() - Translates plural strings
        These functionss mark selected strings as translatable
        Example code: 3-app.py
        babel.cfg was instantiated with the ffg:
        pybabel extract -F babel.cfg -o messages.pot
        pybabel init -i messages.pot -d translations -l en (creates a catalogue for specific eg english translation files)
        pybabel init -i messages.pot -d translations -l fr (creates a catalogue for specific eg french2 translation files)

        Summary
        Extract (pybabel extract): Gather all translatable text from your codebase.
        Initialize (pybabel init): Set up .po files for each target language using the template from messages.pot

        Edit your changes in the .po translation files. Then compile:
        pybabel compile -d translations

        Finally, initialized translation files in compiled to .mo files
"""
