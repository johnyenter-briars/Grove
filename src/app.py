from flask import Flask
from flask import request, redirect
from flask import render_template
from services.DatabaseService import DatabaseService

import os

app = Flask(__name__)
database = DatabaseService()

@app.route('/')
def hello():
    for project in database.getStudentProject(3):
        print(project.getProjectID(), " ", project.getProjectDesc())
    return render_template("index.html", appName="The Grove")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/task')
def task():
    return render_template("task.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

if __name__ == '__main__':
    app.run()
   



