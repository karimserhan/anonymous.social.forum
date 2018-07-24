"""Web server configuration"""

import os
import urllib

db_params = urllib.parse.quote_plus('Driver={SQL Server};Server=tcp:anonymatch.database.windows.net,1433;Database=anonymatchdb;uid=anonymatchuser;pwd=@nonyMatch')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI='mssql+pyodbc:///?odbc_connect={}'.format(db_params)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False