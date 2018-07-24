"""Web server configuration"""

import os
import urllib

params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=anonymatch.database.windows.net;DATABASE=anonymatchdb;UID=anonymatchuser;PWD=@nonyMatch")

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=%s' % params
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False