from flask import Flask, flash, render_template, g, redirect, url_for

from app import app
from app import db
from app.models import Event
from forms import CreateEventForm
#from werkzeug.utils import secure_filename

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',events=Event.getnext(x=4))

@app.route('/activiteiten')
def activiteiten():
    return render_template('activiteiten.html',events=Event.getnext())

@app.route('/activiteit/<event_id>')
def activiteit(event_id):
    event=Event.query.get_or_404(event_id)
    return render_template('activiteit.html',event=event)
    
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
        flash("Event created succesfully")
        form.populate_obj(event)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for("bestuur"))
    return render_template('newevent.html',form=form)