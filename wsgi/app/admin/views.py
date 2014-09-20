# -*- coding: utf8 -*-
"""
@author:    Matthias Feys (matthias.feys@gmail.com)
@date:      %(date)
"""
import logging
from flask import flash, redirect, render_template, g, url_for, request
from app import db
from app.models import Event, Boardmember

from . import admin
from flask.ext.principal import Permission, RoleNeed
from forms import CreateEventForm, CreateBestuurslidForm
#from werkzeug.utils import secure_filename


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger=logging.getLogger("TODO")


@admin.route('/')
@admin.route('/index')
def index():
    events=Event.query.all()
    return render_template('adminindex.html',events=events)

@admin.route('/event/new', methods = ['GET', 'POST'])
def newevent():
    form = CreateEventForm()
    event=Event()
    if form.validate_on_submit():
        form.populate_obj(event)
        db.session.add(event)
        db.session.commit()
        flash("Event created succesfully")
        return redirect(url_for("admin.newevent"))
    return render_template('newevent.html',form=form)

@admin.route('/event/edit/<event_id>', methods = ['GET', 'POST'])
def editevent(event_id=None):
    event=Event.query.get_or_404(event_id)
    form = CreateEventForm(obj=event)
    if form.validate_on_submit():
        form.populate_obj(event)
        db.session.add(event)
        db.session.commit()
        flash("Event edited succesfully")
        return redirect(url_for("admin.index"))
    return render_template('newevent.html',form=form)

@admin.route('/bestuurslid/new', methods = ['GET', 'POST'])
def newbestuurslid():
    form = CreateBestuurslidForm()
    event=Event()
    if form.validate_on_submit():
        form.populate_obj(event)
        db.session.add(event)
        db.session.commit()
        flash("Bestuurslid created succesfully")
        return redirect(url_for("admin.index"))
    return render_template('newbestuurslid.html',form=form)

@admin.route('/bestuurslid/edit/<bestuurslid_id>', methods = ['GET', 'POST'])
def editevent(bestuurslid_id=None):
    bestuurslid=Boardmember.query.get_or_404(bestuurslid_id)
    form = CreateBestuurslidForm(obj=bestuurslid)
    if form.validate_on_submit():
        form.populate_obj(bestuurslid)
        db.session.add(bestuurslid)
        db.session.commit()
        flash("Bestuurlid edited succesfully")
        return redirect(url_for("admin.index"))
    return render_template('newbestuurslid.html',form=form)