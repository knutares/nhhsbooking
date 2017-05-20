from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('app.db')

@app.route('/')
def index():
    return render_template('registrering.html')

@app.route('/medlemsliste')
def medlemsliste():
    db = connect_db()
    cur = db.execute("select fornavn, etternavn from medlemmer")
    entries = [dict(name=row[0], etternavn=row[1]) for row in cur.fetchall()]
    print(entries)
    db.close
    return render_template('medlemsliste.html', entries=entries)

@app.route('/leggtilbruker')
def leggtilbruker():
    fornavn = request.args.get('fornavn')
    etternavn = request.args.get('etternavn')
    db = connect_db()
    sql = "INSERT INTO medlemmer (fornavn, etternavn) values (?,?)"
    db.execute(sql, [fornavn, etternavn])
    db.commit()
    db.close()
    return render_template('profil.html', html_page_fornavn=fornavn, html_page_etternavn=etternavn)

if __name__ == '__main__':
    app.run()
