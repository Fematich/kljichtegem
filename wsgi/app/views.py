from flask import Flask, flash, render_template, g, redirect, url_for, Response

from app import app
from app import db
from app.models import Event, Boardmember
#from werkzeug.utils import secure_filename
from config import EVENTS_PER_PAGE

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',events=Event.getnext(x=3))

@app.route('/activiteiten/<int:page>')
@app.route('/activiteiten')
def activiteiten(page=1):
    return render_template('activiteiten.html',events=Event.getnext(items=False).paginate(page, EVENTS_PER_PAGE, False))

@app.route('/activiteit/<event_id>')
def activiteit(event_id):
    event=Event.query.get_or_404(event_id)
    return render_template('activiteit.html',event=event,events=Event.getnext(x=3))
    
@app.route('/bestuur')
def bestuur():
    return render_template('bestuur.html',bestuursleden=Boardmember.query.all())

@app.route('/nachtvantwodkapje')
def feestweekend():
    return render_template('feestweekend.html')

@app.route('/lidworden')
def lidworden():
    return render_template('lidworden.html',events=Event.getnext(x=3))
    
@app.route('/calendar.ics')
def calendar():
    evs=Event.getics()
    return Response(evs, mimetype='text/ics')
