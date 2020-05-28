from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database
from datetime import datetime
from time import gmtime, strftime

@app.route('/award')
def awardapplespage():
    sess = json.loads(session['user_auth'])
    if not sess:
        return redirect('/')
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    projectID = sess.get('_ProjectID')
    profileID = sess.get('_StudentID')
    print(profileID)
    visibleStudents = []
    validPage = 0

    if session['user_type'] == "STUDENT":
        validPage = 10 - database.getStudent(profileID).getApplesAwarded()
        for student in database.getStudentsOnProject(projectID):
            if(student.getStudentID() != profileID):
                visibleStudents.append(student)
    elif session['user_type'] == "TEACHER":
        for project in database.getProjectsForTeacher(sess.get('_TeacherID')):
                visibleStudents += database.getStudentsOnProject(project.getProjectID())
        validPage = len(visibleStudents)

    possibleApples = database.getValidAppleTypes()

    return render_template("awardapples.html", projectID=projectID, 
                            name='{} {}'.format(first, last),profileID=profileID,
                            visibleStudents=visibleStudents, possibleApples=possibleApples, validPage = validPage)

@app.route('/awardapples', methods=['POST'])
def awardapple():
    sess = json.loads(session['user_auth'])
    if not sess:
        return redirect('/')
    student = sess.get('_StudentID')
    for key,value in request.form.items():
        targetProject = database.getStudentProject(int(key))
        if(student != None):
            database.updateAwardedApples(student)
        database.insertAward(int(key), value, targetProject.getProjectName(), strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    sess = json.loads(session['user_auth'])
    profileID = sess.get('_StudentID')
    not_ugly_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    database.insertAward(profileID, "Red", "Being Humble", not_ugly_time)

    return redirect(url_for("awardapplespage"))