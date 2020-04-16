from flask import Flask
from flask import request, redirect
from flask import render_template
from services.DatabaseService import DatabaseService

import os

app = Flask(__name__)
database = DatabaseService()

print("Home: " +os.getcwd())

@app.route('/')
def hello():
    for teacher in database.getTeachers():
        print(teacher.getFirstName())
    return render_template("index.html", appName="The Grove")

@app.route('/home')
def projects():
    return render_template("home.html")

if __name__ == '__main__':
    app.run()
   



