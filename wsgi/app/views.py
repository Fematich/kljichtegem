from flask import Flask, flash, render_template, g

from app import app

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
