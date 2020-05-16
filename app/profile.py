from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database
from exceptions.NoProfileIDException import NoProfileIDException

@app.route('/profile/')
def profile():
    if request.args.get('profileID') == None:
        raise NoProfileIDException
    sess = json.loads(session['user_auth'])
    if not sess:
        return redirect('/')
    ufirst = sess.get('_FirstName')
    ulast = sess.get('_LastName')
    userName = ufirst + ' ' + ulast
    profileID = sess.get('_StudentID')
    currentProfileID = request.args.get('profileID')
    sess = json.loads(session['user_auth'])
    branches = database.getBranchesForStudent(currentProfileID)
    awards = database.getAwardsForStudent(currentProfileID)
    tasks = database.getTasksForStudent(currentProfileID)
    first = database.getStudent(currentProfileID).getFirstName() 
    last = database.getStudent(currentProfileID).getLastName() 
    return render_template("profile.html", userName=userName, profileName=first+' '+last, branches=branches, awards=awards, tasks=tasks, profileID=profileID)
