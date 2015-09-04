# -*- coding: utf8 -*-
"""
@author:    Matthias Feys (matthias.feys@gmail.com)
@date:      %(date)
"""
import logging
from flask import flash, redirect, render_template, g, url_for, request, jsonify
from app import db
from app.models import Event, Boardmember, Carouselimage, Pagetext

from . import admin
from flask.ext.principal import Permission, RoleNeed
from forms import CreateEventForm, CreateBestuurslidForm, CreateCarouselimagesForm, CreatePagetextForm
#from werkzeug.utils import secure_filename


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger=logging.getLogger("TODO")

@admin.route('/')
@admin.route('/index/<tab>')
@admin.route('/index')
def index(tab="activiteiten"):
    ptxt1=Pagetext.query.get_or_404(1)
    ptxt2=Pagetext.query.get_or_404(2)
    ptxt3=Pagetext.query.get_or_404(3)
    return render_template('adminindex.html',events=Event.getnext(),
        bestuursleden=Boardmember.query.all(),
        carouselimages=Carouselimage.query,
        pagetext=Pagetext.query,
        introtekst_form=CreatePagetextForm(obj=ptxt1),
        fuiftekst_form = CreatePagetextForm(obj=ptxt2),
        lidworden_form = CreatePagetextForm(obj=ptxt3),
        tab=tab)

@admin.route('/event/new', methods = ['GET', 'POST'])
def newevent():
    form = CreateEventForm()
    event=Event()
    if form.validate_on_submit():
        form.populate_obj(event)
        event.image=event.image.replace("https://www.dropbox.com","https://dl.dropboxusercontent.com/")
        db.session.add(event)
        db.session.commit()
        flash("Event created succesfully")
        return redirect(url_for("admin.index"))
    return render_template('newevent.html',form=form)

@admin.route('/event/edit/<event_id>', methods = ['GET', 'POST'])
def editevent(event_id=None):
    event=Event.query.get_or_404(event_id)
    form = CreateEventForm(obj=event)
    if form.validate_on_submit():
        form.populate_obj(event)
        event.image=event.image.replace("https://www.dropbox.com","https://dl.dropboxusercontent.com/")
        db.session.add(event)
        db.session.commit()
        flash("Event edited succesfully")
        return redirect(url_for("admin.index"))
    return render_template('newevent.html',form=form)

@admin.route('/event/copy/<event_id>', methods = ['GET', 'POST'])
def copyevent(event_id=None):
    new_event=Event()
    event=Event.query.get_or_404(event_id)
    new_event.title=event.title
    new_event.image=event.image
    new_event.description=event.description
    new_event.begin=event.begin
    new_event.end=event.end
    new_event.location=event.location
    new_event.price=event.price
    form = CreateEventForm(obj=new_event)
    if form.validate_on_submit():
        form.populate_obj(new_event)
        new_event.image=new_event.image.replace("https://www.dropbox.com","https://dl.dropboxusercontent.com/")
        db.session.add(new_event)
        db.session.commit()
        flash("Event edited succesfully")
        return redirect(url_for("admin.index"))
    return render_template('newevent.html',form=form)


@admin.route('/event/delete/<event_id>', methods = ['GET','POST'])
def deleteevent(event_id=None):
    event=Event.query.get(event_id)
    db.session.delete(event)
    db.session.commit()
    flash("Event deleted")
    return redirect(url_for('admin.index'))

@admin.route('/bestuurslid/new', methods = ['GET', 'POST'])
def newbestuurslid():
    form = CreateBestuurslidForm()
    bestuurslid=Boardmember()
    if form.validate_on_submit():
        form.populate_obj(bestuurslid)
        db.session.add(bestuurslid)
        db.session.commit()
        flash("Bestuurslid created succesfully")
        return redirect(url_for("admin.index",tab="bestuur"))
    return render_template('newbestuurslid.html',form=form)

@admin.route('/bestuurslid/edit/<bestuurslid_id>', methods = ['GET', 'POST'])
def editbestuurslid(bestuurslid_id=None):
    bestuurslid=Boardmember.query.get_or_404(bestuurslid_id)
    form = CreateBestuurslidForm(obj=bestuurslid)
    if form.validate_on_submit():
        form.populate_obj(bestuurslid)
        db.session.add(bestuurslid)
        db.session.commit()
        flash("Bestuurlid edited succesfully")
        return redirect(url_for("admin.index",tab="bestuur"))
    return render_template('newbestuurslid.html',form=form)
    
@admin.route('/bestuurslid/delete/<bestuurslid_id>', methods = ['GET','POST'])
def deletebestuurslid(bestuurslid_id=None):
    bestuurslid=Boardmember.query.get(bestuurslid_id)
    db.session.delete(bestuurslid)
    db.session.commit()
    flash("Bestuurslid deleted")
    return redirect(url_for('admin.index',tab="bestuur"))

@admin.route('/homepagecarousel/new', methods = ['GET', 'POST'])
def newhomepagecarouselimage():
    form = CreateCarouselimagesForm()
    cmg=Carouselimage()
    cmg.carousel="homepage"
    if form.validate_on_submit():
        form.populate_obj(cmg)
        cmg.image=cmg.image.replace("https://www.dropbox.com","https://dl.dropboxusercontent.com/")
        db.session.add(cmg)
        db.session.commit()
        flash("Image created succesfully")
        return redirect(url_for("admin.index",tab="startpagina"))
    return render_template('newcarouselimage.html',form=form)

@admin.route('/fuifcarousel/new', methods = ['GET', 'POST'])
def newfuifcarouselimage():
    form = CreateCarouselimagesForm()
    cmg=Carouselimage()
    cmg.carousel="fuif"
    if form.validate_on_submit():
        form.populate_obj(cmg)
        cmg.image=cmg.image.replace("https://www.dropbox.com","https://dl.dropboxusercontent.com/")
        db.session.add(cmg)
        db.session.commit()
        flash("Image created succesfully")
        return redirect(url_for("admin.index",tab="fuifweekend"))
    return render_template('newcarouselimage.html',form=form)

@admin.route('/carousel/edit/<image_id>', methods = ['GET', 'POST'])
def editcarouselimage(image_id=None):
    cmg=Carouselimage.query.get_or_404(image_id)
    form = CreateCarouselimagesForm(obj=cmg)
    if form.validate_on_submit():
        form.populate_obj(cmg)
        cmg.image=cmg.image.replace("https://www.dropbox.com","https://dl.dropboxusercontent.com/")
        db.session.add(cmg)
        db.session.commit()
        flash("Image edited succesfully")
        if cmg.carousel=="homepage":
            return redirect(url_for("admin.index",tab="startpagina"))
        else:
            return redirect(url_for("admin.index",tab="fuifweekend"))
    return render_template('newcarouselimage.html',form=form)

@admin.route('/carousel/delete/<image_id>', methods = ['GET','POST'])
def deletecarouselimage(image_id=None):
    cmg=Carouselimage.query.get(image_id)
    cmg_carousel=cmg.carousel
    db.session.delete(cmg)
    db.session.commit()
    flash("Image deleted")
    if cmg_carousel=="homepage":
        return redirect(url_for("admin.index",tab="startpagina"))
    else:
        return redirect(url_for("admin.index",tab="fuifweekend"))

@admin.route('/introtekst/edit', methods = ['GET', 'POST'])
def editintrotekst():
    ptxt=Pagetext.query.get_or_404(1)
    form = CreatePagetextForm(obj=ptxt)
    if form.validate_on_submit():
        form.populate_obj(ptxt)
        db.session.add(ptxt)
        db.session.commit()
        flash("Introtext edited succesfully")
        return redirect(url_for("admin.index",tab="startpagina"))
    return redirect(url_for("admin.index",tab="startpagina"))

@admin.route('/fuiftekst/edit', methods = ['GET', 'POST'])
def editfuiftekst():
    ptxt=Pagetext.query.get_or_404(2)
    form = CreatePagetextForm(obj=ptxt)
    if form.validate_on_submit():
        form.populate_obj(ptxt)
        db.session.add(ptxt)
        db.session.commit()
        flash("Fuiftekst edited succesfully")
        return redirect(url_for("admin.index",tab="fuifweekend"))
    return render_template('newtext.html',form=form)

@admin.route('/lidworden/edit', methods = ['GET', 'POST'])
def editlidwordentekst():
    ptxt=Pagetext.query.get_or_404(3)
    form = CreatePagetextForm(obj=ptxt)
    if form.validate_on_submit():
        form.populate_obj(ptxt)
        db.session.add(ptxt)
        db.session.commit()
        flash("Lid worden tekst edited succesfully")
        return redirect(url_for("admin.index",tab="lidworden"))
    return render_template('newtext.html',form=form)

@admin.route('/quiz/edit', methods = ['GET', 'POST'])
def editquiztekst():
    ptxt=Pagetext.query.get_or_404(4)
    form = CreatePagetextForm(obj=ptxt)
    if form.validate_on_submit():
        form.populate_obj(ptxt)
        db.session.add(ptxt)
        db.session.commit()
        flash("Quiz tekst edited succesfully")
        return redirect(url_for("admin.index",tab="lidworden"))
    return render_template('newtext.html',form=form)