from flask import Flask
from flask import request, redirect
from flask import render_template
from services.DatabaseService import DatabaseService

import os

app = Flask(__name__)
database = DatabaseService()


@app.route('/',methods=['POST','GET'])

def hello():
    """for project in database.getStudentProject(3):
        print(project.getProjectID(), " ", project.getProjectDesc())
    """
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        shouldLogin = False
        for user in database.getUserCredentials():
            u = user._UserName
            p = user._UserPass
            if u == username and p == password:
                shouldLogin = True
            elif u == username and p != password:
                return render_template('index.html', loggedInUser="Incorrect password")
        if(shouldLogin):
            return render_template('index.html', loggedInUser="Welcome, "+username)
        else:
            return render_template('index.html', loggedInUser="User does not exist")
    return render_template("index.html", loggedInUser="Please login below")

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/task')
def task():
    return render_template("task.html")


@app.route('/profile')
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run()
