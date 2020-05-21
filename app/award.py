from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database
from datetime import datetime

@app.route('/award')
def awardapplespage():
    sess = json.loads(session['user_auth'])
    if not sess:
        return redirect('/')
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    projectID = sess.get('_ProjectID')
    profileID = sess.get('_StudentID')
    visibleStudents = []

    if session['user_type'] == "STUDENT":
        visibleStudents = database.getStudentsOnProject(projectID)
    elif session['user_type'] == "TEACHER":
        for project in database.getProjectsForTeacher(sess.get('_TeacherID')):
            visibleStudents += database.getStudentsOnProject(project.getProjectID())

    possibleApples = database.

    return render_template("awardapples.html", projectID=projectID, 
                            name='{} {}'.format(first, last),profileID=profileID,
                            visibleStudents=visibleStudents)

@app.route('/awardapples', methods=['POST'])
def awardapple():
    for key,value in request.form.items():
        targetProject = database.getStudentProject(int(key))
        database.insertAward(int(key), value, targetProject.getProjectName(), datetime.now())

    return redirect(url_for("awardapplespage"))