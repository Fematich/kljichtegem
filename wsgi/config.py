import os

SQLALCHEMY_DATABASE_URI = os.environ['OPENSHIFT_POSTGRESQL_DB_URL']
SQLALCHEMY_ECHO = False

################################################################
######################## form settings #########################
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

DEBUG = True
