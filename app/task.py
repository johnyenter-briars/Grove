from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database
from exceptions.NoTaskIDException import NoTaskIDException
from werkzeug.utils import secure_filename
from models.Branch import Branch
from datetime import datetime


UPLOAD_FOLDER = '/app/static/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@app.route('/task/', methods=['POST', 'GET'])
def task():
    if request.args.get('taskID') == None:
        raise NoTaskIDException
    currentTaskID = request.args.get('taskID')
    files = database.getFilesForTask(currentTaskID)
    messages = database.getChatForTask(currentTaskID)

    sess = json.loads(session['user_auth'])
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    fullName = first + " " + last
    if request.method == 'POST' and request.form.getlist("message") == [] and request.form.getlist("filename") == [] :
        file = request.files['fileType']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            database.addFile(currentTaskID, filename, file.read())
            return redirect('/task/?taskID='+currentTaskID)

    if request.method == 'POST' and request.form.getlist("message") != []:
        now = datetime.now()
        current_time = now.strftime("%x %I:%M:%S %p")
        newChat = request.form['message']
        database.addMessage(fullName, currentTaskID, current_time, newChat)
        return redirect('/task/?taskID='+currentTaskID)

    if request.method == 'POST':
        fname = request.form['filename']
        database.removeFile(fname)
        return redirect('/task/?taskID='+currentTaskID)

    return render_template("task.html", 
        name=first+' '+last, files=files, 
        taskObj=database.getTask(int(currentTaskID)),
        taskID='?taskID='+currentTaskID,
        messages=messages,
    )

@app.route('/task/addtasktobranch', methods=['POST'])
def addTaskToBranch():
    taskTitle = request.form["title"]
    studentOnTaskId = int(request.form["user"])
    branchId = request.args.get("branchID")
    projectId = request.args.get("projectID")
    
    database.insertNewTask(branchId, studentOnTaskId, projectId, taskTitle)

    return redirect(url_for("projects"))



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS