# -*- coding: utf8 -*-
"""
@author:    Matthias Feys (matthiasfeys@gmail.com)
@date:      %(date)
"""
import logging
from app import app, db
#from flask.ext.security import UserMixin, RoleMixin

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger=logging.getLogger("TODO")

#roles_users = db.Table('roles_users',
#        db.Column('user_id', db.Integer(), db.ForeignKey('user.id',onupdate="cascade")),
#        db.Column('role_id', db.Integer(), db.ForeignKey('role.id',onupdate="cascade")))
#
#class User(db.Model, UserMixin):
#    id = db.Column(db.Integer, primary_key=True)
#    email = db.Column(db.String(120), index = True, unique = True)
#    password = db.Column(db.String(60))
#    active = db.Column(db.Boolean())
#    confirmed_at = db.Column(db.DateTime())
#    roles = db.relationship('Role', secondary=roles_users,
#                            backref=db.backref('users', lazy='dynamic'))
#
#    def __repr__(self):
#        return '<User %r>' % (self.username())    
#
#class Role(db.Model, RoleMixin):
#    id = db.Column(db.Integer(), primary_key=True)
#    name = db.Column(db.String(80), unique=True)
#    description = db.Column(db.String(255))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    image = db.Column(db.String(512))
    description = db.Column(db.String(512))
    #timestamp = db.Column(db.DateTime())
    location = db.Column(db.String(120))
    price = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Activiteit %r>' % (self.title)

class Boardmember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    image = db.Column(db.String(512))
    function = db.Column(db.String(512))
    email = db.Column(db.String(120))
    facebook = db.Column(db.String(120))
    cellphone = db.Column(db.String(15))
    
    def __repr__(self):
        return '<bestuurslid %r>' % (self.name)