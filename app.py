from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('json.html')
"""
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

@app.route('/logginn')
def medlemsliste():
    return render_template('kalender.html')
"""

@app.route('/data')
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')

    with open("events.json", "r") as input_data:
        return input_data.read()

if __name__ == '__main__':
    app.run()
