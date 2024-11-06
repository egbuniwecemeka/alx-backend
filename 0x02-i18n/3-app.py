#!/usr/bin/env python3
""" A python script that parametrizes templates based on translations """

from flask import Flask
from flask_babel import gettext, ngettext


app = Flask(__name__)