# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from email.policy import default
from unicodedata import name
import babel
import dateutil.parser
import json
import logging

from datetime import datetime
from flask import Flask, render_template, request, Response, flash, redirect, url_for, Blueprint
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form, CSRFProtect
from logging import Formatter, FileHandler
from .forms import *
from .config import app_config
from .services.utils.format_datetime import format_datetime

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config['SECRET_KEY'] = app_config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = app_config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = app_config['SQLALCHEMY_TRACK_MODIFICATIONS']
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
migrate = Migrate(app, db)

app.jinja_env.filters['datetime'] = format_datetime


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
