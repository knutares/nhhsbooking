from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('app.db')

@app.route('/')
def index():
    return render_template('startside.html')

@app.route('/bekreftelse')
def index():
    return render_template('mb_bekreftelsesside.html')

@app.route('/skjema')
def index():
    return render_template('mb_utfyllingskjema.html')

@app.route('/moterombooking')
def index():
    return render_template('moterombooking.html')

@app.route('/velgtid')
def index():
    return render_template('velgtidrom.html')

@app.route('/logginn')
def medlemsliste():
    return render_template('loginn.html')

if __name__ == '__main__':
    app.run()
