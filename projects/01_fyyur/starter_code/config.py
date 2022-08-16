import os

app_config = {'SECRET_KEY': os.urandom(32), 'DEBUG': True,
              'SQLALCHEMY_DATABASE_URI': 'postgresql://postgres:Password01!@localhost:5432/fyyur',
              'SQLALCHEMY_TRACK_MODIFICATIONS': False,
              'WTF_CSRF_SECRET_KEY': os.urandom(30)}

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
