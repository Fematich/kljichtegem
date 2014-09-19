from flask import Flask  
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)  
app.config.from_object('config')
db = SQLAlchemy(app)

#from app import views






from views import *

#from app import admin
#app.register_blueprint(admin.admin,url_prefix='/admin')