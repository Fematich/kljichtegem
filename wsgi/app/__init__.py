from flask import Flask  
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)  
app.config.from_object('config')
db = SQLAlchemy(app)

from models import User, Role
from momentjs import momentjs
# flask-security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# jinja globals
app.jinja_env.globals['momentjs'] = momentjs

from views import *

from app import admin
app.register_blueprint(admin.admin,url_prefix='/admin')
