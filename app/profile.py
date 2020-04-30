from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database

@app.route('/profile')
def profile():
    sess = json.loads(session['user_auth'])
    branches = database.getBranchesForStudent(sess.get('_StudentID'))
    awards = database.getAwardsForStudent(sess.get('_StudentID'))
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    return render_template("profile.html", name=first+' '+last, branches=branches, awards=awards)
