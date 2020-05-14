from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database

@app.route('/profile/')
def profile():
    currentProfileID = request.args.get('profileID')
    sess = json.loads(session['user_auth'])
    branches = database.getBranchesForStudent(currentProfileID)
    awards = database.getAwardsForStudent(currentProfileID)
    tasks = database.getTasksForStudent(currentProfileID)
    first = database.getStudent(currentProfileID).getFirstName() 
    last = database.getStudent(currentProfileID).getLastName() 
    return render_template("profile.html", name=first+' '+last, branches=branches, awards=awards, tasks=tasks)
