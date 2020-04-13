from flask import Flask
from flask import request, redirect
from flask import render_template
import sqlite3
from flask import g

app = Flask(__name__)
_db = None
# database = DatabaseService(
DATABASE = 'database_files/Grove.db'

def get_db():
    _db = getattr(g, '_database', None)
    if _db is None:
        _db = g._database = sqlite3.connect(DATABASE)
    return _db


@app.teardown_appcontext
def close_connection(exception):
    _db = getattr(g, '_database', None)
    if _db is not None:
        _db.close()


@app.route('/')
def hello():
    db = get_db()
    print(db.execute("select * from students;").fetchall())
    return render_template("index.html", appName="The Grove")

if __name__ == '__main__':
    app.run()
   



