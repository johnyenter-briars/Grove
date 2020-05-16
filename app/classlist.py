from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database

@app.route('/classlist')
def classlist():
    sess = json.loads(session['user_auth'])
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    teachID = sess.get('_TeacherID')
    profileID = sess.get('_StudentID')
    projectID = sess.get('_ProjectID')

    students = database.getClassList(teachID)
    
    return render_template("classlist.html", students=students, name=first+' '+last, profileID=profileID,projectID=projectID)