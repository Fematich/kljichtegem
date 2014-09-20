from flask import Flask, flash, render_template, g, redirect, url_for, Response

from app import app
from app import db
from app.models import Event, Boardmember
from forms import CreateEventForm
#from werkzeug.utils import secure_filename

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',events=Event.getnext(x=3))

@app.route('/activiteiten')
def activiteiten():
    return render_template('activiteiten.html',events=Event.getnext())

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
    evs='BEGIN:VCALENDAR\nPRODID:ics.py - http://git.io/lLljaA\nVERSION:2.0\nBEGIN:VEVENT\nDTSTAMP:20140920T231510Z\nDTSTART:20150101T000000Z\nSUMMARY:My cool event\nUID:dd247d5c-342a-4e45-a1a6-f1bd3af71bb1@dd24.org\nEND:VEVENT\nEND:VCALENDAR'
    return Response(evs, mimetype='text/ics')
