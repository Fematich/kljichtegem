import os

################################################################
#################### SQLAlchemy settings #######################
SQLALCHEMY_DATABASE_URI = os.environ['OPENSHIFT_POSTGRESQL_DB_URL']
SQLALCHEMY_ECHO = False

################################################################
######################## form settings #########################
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

################################################################
######################## login settings ########################
SECURITY_POST_LOGIN_VIEW='/admin'



DEBUG = True
