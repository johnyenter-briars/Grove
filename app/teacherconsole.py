from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database

@app.route('/teacherconsole')
def teacherconsole():
    sess = json.loads(session['user_auth'])
    if not sess:
        return redirect('/')
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    tasksToReview = database.getTasksToBeReviewed

    return render_template("teacherconsole.html", name=first, taskToReview=tasksToReview)

@app.route('/addstudent/', methods=['POST', 'GET'])
def addStudent():
    if request.method == 'POST':
        fname = request.form['studentFName']
        lname = request.form['studentLName']
        projID = request.form['projectID']

        database.insertNewStudent(
            fname, lname, 
            int(json.loads(session['user_auth']).get('_TeacherID')), 
            int(projID), "perm0")
    
    return render_template("teacherconsole.html", 
            name = json.loads(session['user_auth']).get('_FirstName'))