from flask import Flask, request, redirect, render_template, json, session, jsonify
from config import Config
from services.DatabaseService import DatabaseService
from services.JSONEncoderService import ClassEncoder

import os
from flask.helpers import url_for

app = Flask(__name__)
app.config.from_object(Config)

database = DatabaseService()
@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
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
            # add session persistance
            # This code assumes the user is a student
            userObject = [ele for ele in database.getUserCredentials(
            ) if ele.getUserName() == username and ele.getUserPass() == password][0]
            if userObject.getUserType() == "Student":
                session['user_auth'] = ClassEncoder().encode(
                    database.getStudent(userObject.getUserID()))
            elif userObject.getUserType() == "Teacher":
                session['user_auth'] = ClassEncoder().encode(
                    database.getTeacher(userObject.getUserID()))
            return redirect(url_for('home'))
        else:
            return render_template('index.html', loggedInUser="User does not exist")

    return render_template("index.html", loggedInUser="Please login below")


@app.route('/home')
def home():
    sess = json.loads(session['user_auth'])
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    return render_template("home.html", name=first+' '+last)


@app.route('/projects')
def projects():
    sess = json.loads(session['user_auth'])
    if not sess:
        return redirect('/')
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    teacherObj = database.getTeacher(sess.get('_TeacherID'))
    pId = sess.get('_ProjectID')
    perm = sess.get('_PermissionLevel')

    branches = database.getBranchesForProject(pId)
    

    return render_template("projects.html", name=first+' '+last, 
        teach=teacherObj.getFirstName() + " " + teacherObj.getLastName(), 
        proj=pId, perm=perm,
        branches=rawBranches


@app.route('/task')
def task():
    sess = json.loads(session['user_auth'])
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    return render_template("task.html", name=first+' '+last)


@app.route('/profile')
def profile():
    sess = json.loads(session['user_auth'])
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    return render_template("profile.html", name=first+' '+last)

@app.route('/logout')
def logout():
    session.pop('user_auth')
    return redirect('/')

@app.errorhandler(KeyError)
def keyerror_exception_handler(error):
    return render_template('keyerror.html')

if __name__ == '__main__':
    app.run(debug=True)
