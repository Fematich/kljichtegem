import os

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
SECURITY_POST_LOGIN_VIEW='/admin'


EVENTS_PER_PAGE=6

DEBUG = True

if 'OPENSHIFT_POSTGRESQL_DB_HOST' in os.environ:
    pg_url = 'postgresql://%s:%s/%s' % (
        os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
        os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
        os.environ['OPENSHIFT_APP_NAME'])