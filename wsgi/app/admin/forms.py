# -*- coding: utf8 -*-
"""
@author:    Matthias Feys (matthiasfeys@spurrit.com), Spurrit
@date:      %(date)
"""
import logging
#from wtforms.ext.sqlalchemy.orm import model_form
from app import app
#from flask.ext.uploads import UploadSet, IMAGES, configure_uploads
from wtforms import DateTimeField, TextAreaField, TextField, IntegerField
#from flask_wtf.file import FileField, FileAllowed
from flask.ext.wtf import Form
from wtforms.validators import Required


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger=logging.getLogger("TODO")

class CreateEventForm(Form):
    title = TextField('title', validators = [Required()])
    image = TextField('image')
    description = TextAreaField('description')
    date = DateTimeField('date', validators=[Required()], format='%d/%m/%Y')
    location = TextAreaField('location')
    price = IntegerField()

class CreateBestuurslidForm(Form):
    name = TextField('naam', validators = [Required()])
    image = TextField('image')
    function = TextField('function')
    email = TextField('email')
    facebook = TextField('facebook')
    cellphone = TextField('cellphone')