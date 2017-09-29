import os
import logging

logging.info(str(os.environ))
################################################################
#################### SQLAlchemy settings #######################
SQLALCHEMY_DATABASE_URI = os.environ['postgresql_SERVICE_HOST']
SQLALCHEMY_ECHO = False

################################################################
######################## form settings #########################
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

################################################################
######################## login settings ########################
SECURITY_POST_LOGIN_VIEW = '/admin'


EVENTS_PER_PAGE = 6

DEBUG = True
