from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database
from exceptions.NoProfileIDException import NoProfileIDException

@app.route('/profile/')
def profile():
    if request.args.get('profileID') == None:
        raise NoProfileIDException
    currentProfileID = request.args.get('profileID')
    sess = json.loads(session['user_auth'])
    studentID = sess.get('_StudentID')
    teacherID = sess.get('_TeacherID')
    branches = database.getBranchesForStudent(currentProfileID)
    awards = database.getAwardsForStudent(currentProfileID)
    tasks = database.getTasksForStudent(currentProfileID)
    first = database.getStudent(currentProfileID).getFirstName() 
    last = database.getStudent(currentProfileID).getLastName() 
    return render_template("profile.html", name=first+' '+last, branches=branches, awards=awards, tasks=tasks, studentID=studentID, teacherID=teacherID)
