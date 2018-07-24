"""
The flask application package.
"""

from flask import Flask
from WebProject.config import Config
import logging

app = Flask(__name__)
@app.before_first_request
def setup_logging():
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        formatter = logging.Formatter('>>>>>>>>>>>>> %(asctime)s %(levelname)s - %(message)s', '[%d/%b/%Y %H:%M:%S]')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)
        app.logger.setLevel(logging.DEBUG)

app.logger.setLevel(logging.DEBUG)

app.config.from_object(Config)

#app.debug = True

import WebProject.views
