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
from wtforms.validators import Required, Length


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger=logging.getLogger("TODO")

class CreateEventForm(Form):
    title = TextField('title', validators = [Required(),Length(max=255)])
    image = TextField('image',validators=[Length(max=512)])
    description = TextAreaField('description',validators=[Length(max=1024)])
    begin = DateTimeField('date', validators=[Required()], format='%d/%m/%Y %H:%M')
    end = DateTimeField('date', validators=[Required()], format='%d/%m/%Y %H:%M')
    location = TextAreaField('location',default="KLJ lokaal, Kasteelwegel 1",validators=[Length(max=120)])
    price = TextField('price',default="0", validators=[Length(max=20)])

class CreateBestuurslidForm(Form):
    name = TextField('naam', validators = [Required()])
    image = TextField('image')
    function = TextField('function')
    email = TextField('email')
    facebook = TextField('facebook')
    cellphone = TextField('cellphone')

class CreateCarouselimagesForm(Form):
    image = TextField('text',validators=[Length(max=512), Required()])
    title = TextField('text',validators=[Length(max=256)])
    text = TextField('text',validators=[Length(max=512)])

class CreatePagetextForm(Form):
    text = TextAreaField('text',validators=[Length(max=8192)])
