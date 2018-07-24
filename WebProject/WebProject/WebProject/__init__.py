"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from WebProject.config import Config
import logging

app = Flask(__name__)

# Setup log level/formatting
@app.before_first_request
def setup_logging():
    if not app.debug:
        formatter = logging.Formatter('>>>>>>>>>>>>> %(asctime)s %(levelname)s - %(message)s', '[%d/%b/%Y %H:%M:%S]')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)
        app.logger.setLevel(logging.DEBUG)

app.config.from_object(Config)

# setup db and migration F/W
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# setup login F/W
login = LoginManager(app)
login.login_view = 'login'

import WebProject.views, WebProject.models
