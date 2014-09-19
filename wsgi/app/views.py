from flask import Flask, flash, render_template, g, redirect, url_for

from app import app
from app import db
from app.models import Event
from forms import CreateEventForm
#from werkzeug.utils import secure_filename

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/activiteiten')
def activiteiten():
    return render_template('activiteiten.html')
    
@app.route('/bestuur')
def bestuur():
    return render_template('bestuur.html')

@app.route('/nachtvantwodkapje')
def feestweekend():
    return render_template('feestweekend.html')

@app.route('/event/new', methods = ['GET', 'POST'])
def newevent():
    form = CreateEventForm()
    event=Event()
    if form.validate_on_submit():
        form.populate_obj(event)
        db.session.add(event)
        db.session.commit()
        flash("Event created succesfully")
        return redirect(url_for("app.bestuur"))
    else:
        flash("No event created")
    return render_template('newevent.html',form=form)