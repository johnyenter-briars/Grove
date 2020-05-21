from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database

@app.route('/award')
def awardapplespage():
    sess = json.loads(session['user_auth'])
    if not sess:
        return redirect('/')
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    projectID = sess.get('_ProjectID')
    visibleStudents = []

    if session['user_type'] == "STUDENT":
        visibleStudents = database.getStudentsOnProject(projectID)
    elif session['user_type'] == "TEACHER":
        pass

    return render_template("awardapples.html", projectID=projectID, name='{} {}'.format(first, last),
                            visibleStudents=visibleStudents)

@app.route('/awardapples', methods=['POST'])
def awardapple():
    x = request.form

    return redirect(url_for("awardapplespage"))