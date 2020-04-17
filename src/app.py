from flask import Flask
from flask import request, redirect
from flask import render_template
from flask import session
# from flask_session import Session
from config import Config
from services.DatabaseService import DatabaseService
from services.JSONEncoderService import ClassEncoder

import os

app = Flask(__name__)
app.config.from_object(Config)
# sess = Session()
# sess.init_app(app)

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
            #add session persistance
            #This code assumes the user is a student
            userObject = [ele for ele in database.getUserCredentials() if ele.getUserName() == username and ele.getUserPass() == password][0]
            if userObject.getUserType() == "Student":
                session['user_auth'] = ClassEncoder().encode(database.getStudent(userObject.getUserID()))

            return render_template('home.html', loggedInUser="Welcome, "+username)
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
