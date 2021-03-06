# -*- coding: utf8 -*-
"""
@author:    Matthias Feys (matthiasfeys@gmail.com)
@date:      %(date)
"""
import logging, random

from icalendar import Calendar, vText, Event as iEvent
import pytz
from datetime import datetime, timedelta

from app import app, db
from flask.ext.security import UserMixin, RoleMixin


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger=logging.getLogger("TODO")

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id',onupdate="cascade")),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id',onupdate="cascade")))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index = True, unique = True)
    password = db.Column(db.String(60))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User %r>' % (self.username())    

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    image = db.Column(db.String(512))
    description = db.Column(db.String(1024))
    begin = db.Column(db.DateTime())
    end = db.Column(db.DateTime())
    location = db.Column(db.String(120))
    price = db.Column(db.String(20))
    
    def __repr__(self):
        return '<Activiteit %r>' % (self.title)
    
    @staticmethod
    def getnext(x=None,items=True):
        today=datetime.now()
        if x!=None:
            events=Event.query.filter(Event.end>today).order_by(Event.begin).limit(x)
        else:
            events=Event.query.filter(Event.end>today).order_by(Event.begin)
        if items:
            return events.all()
        else:
            return events
    
    @staticmethod
    def getics():
        cal = Calendar()
        cal['summary'] = 'KLJ Ichtegem agenda'
        for evt in Event.query.all():
            ev = iEvent()
            ev.add('dtstart', evt.begin.replace(tzinfo=pytz.timezone("Europe/Brussels")))
            ev.add('dtend', evt.end.replace(tzinfo=pytz.timezone("Europe/Brussels")))
            ev['location'] = vText(evt.location)
            ev.add('summary', evt.title)
            ev.add('description', evt.description+"\nprijs: "+str(evt.price)+" EUR")
            cal.add_component(ev)
        c=cal.to_ical()
        return str(c)

    @staticmethod
    def getNextDate():
        lastDate = Event.query.order_by(Event.begin.desc()).limit(1).first().begin
        print lastDate
        return lastDate + timedelta( (4-lastDate.isoweekday()) % 7 +8)
        
class Boardmember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    image = db.Column(db.String(512))
    function = db.Column(db.String(512))
    email = db.Column(db.String(120))
    facebook = db.Column(db.String(120))
    cellphone = db.Column(db.String(15))

    def fblink(self):
        return "https://www.facebook.com/"+self.facebook

    def getscrambledmail(self):
        if self.email=="":
            return ""
        else:
            return "".join([self.email[i] for i in range(len(self.email)-1,-1,-1)])

    def getscrambledorder(self):
        if self.email=="":
            return ""
        else:
            order=range(len(self.email)-1,-1,-1)
            return str(order)

    def __repr__(self):
        return '<bestuurslid %r>' % (self.name)

class Carouselimage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carousel = db.Column(db.String(512))
    image = db.Column(db.String(512))
    title = db.Column(db.String(256))
    text = db.Column(db.String(512))

class Pagetext(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(2048))
