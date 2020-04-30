from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from config.config import Config
from services.DatabaseService import DatabaseService
from services.JSONEncoderService import ClassEncoder
from werkzeug.utils import secure_filename
from models.Branch import Branch
from exceptions.NoTaskIDException import NoTaskIDException
import os
import sqlite3
from flask.helpers import url_for

UPLOAD_FOLDER = '/static/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

database = DatabaseService()
@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        shouldLogin = False
        for user in database.getUserCredentials():
            u = user._UserName
            p = user._UserPass
            if u == username and p == password:
                shouldLogin = True
            elif u == username and p != password:
                return render_template('index.html', loggedInUser="Incorrect password")

        if(shouldLogin):
            # add session persistance
            # This code assumes the user is a student
            userObject = [ele for ele in database.getUserCredentials(
            ) if ele.getUserName() == username and ele.getUserPass() == password][0]
            if userObject.getUserType() == "Student":
                session['user_auth'] = ClassEncoder().encode(
                    database.getStudent(userObject.getUserID()))
            elif userObject.getUserType() == "Teacher":
                session['user_auth'] = ClassEncoder().encode(
                    database.getTeacher(userObject.getUserID()))
            return redirect(url_for('home'))
        else:
            return render_template('index.html', loggedInUser="User does not exist")

    return render_template("index.html", loggedInUser="Please login below")


@app.route('/home')
def home():
    sess = json.loads(session['user_auth'])
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    return render_template("home.html", name=first+' '+last)


@app.route('/projects')
def projects():
    sess = json.loads(session['user_auth'])
    if not sess:
        return redirect('/')
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    teacherObj = database.getTeacher(sess.get('_TeacherID'))
    pId = sess.get('_ProjectID')
    perm = sess.get('_PermissionLevel')

    branches: List[Branch] = database.getBranchesForProject(pId)
    projectObj = database.getProject(pId)
    studentsOnProject = {}
    rawtasks = []
    tasksByBranchId = {}
    
    #Just getting a list of all students who are on this project
    #I realize there is a better way to do this now, but John from a week ago was dumb
    for branch in branches:
        for studentId in branch.getStudents():
            studentsOnProject[studentId] = database.getStudent(studentId)
    
    for branch in branches:
        rawtasks += database.getTasksForBranch(branch.getBranchID(), branch.getProjectID())
        
    for task in rawtasks:
        if task.getBranchID() in tasksByBranchId:
            tasksByBranchId[task.getBranchID()].append(task)
        else:
            tasksByBranchId[task.getBranchID()] = [task]
   
    return render_template("projects.html", name=first+' '+last, 
        teach=teacherObj.getFirstName() + " " + teacherObj.getLastName(), 
        proj=projectObj, 
        perm=perm,
        branches=branches,
        studentsOnProject=studentsOnProject,
        tasksPerBranch=tasksByBranchId)

@app.route('/task/', methods=['POST', 'GET'])
def task():
    if request.args.get('taskID') == None:
        raise NoTaskIDException
    
    
    files = database.getFilesForTask()
    newID = len(files)
    sess = json.loads(session['user_auth'])
    first = sess.get('_FirstName')
    last = sess.get('_LastName')

    if request.method == 'POST':
        file = request.files['fileType']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #path = app.config['UPLOAD_FOLDER'] + "/"
            #completeName = os.path.join(path, filename)
            #file.save(os.path.join(app.root_path, 'static','files',secure_filename(file.filename)))
            database.addFile(newID,filename, file.read())
            return redirect('/task/?taskID='+request.args.get('taskID') )

    return render_template("task.html", 
        name=first+' '+last, files=files, 
        taskObj=database.getTask(int(request.args.get('taskID'))),
        taskID='?taskID='+request.args.get('taskID') 
    )

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/profile')
def profile():
    sess = json.loads(session['user_auth'])
    branches = database.getBranchesForStudent(sess.get('_StudentID'))
    awards = database.getAwardsForStudent(sess.get('_StudentID'))
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    return render_template("profile.html", name=first+' '+last, branches=branches, awards=awards)

@app.route('/logout')
def logout():
    session.pop('user_auth')
    return redirect('/')

@app.route('/classlist')
def classlist():
    sess = json.loads(session['user_auth'])
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    teachID = sess.get('_TeacherID')
    
    students = database.getClassList(teachID)
    
    return render_template("classlist.html", students=students, name=first+' '+last)

@app.errorhandler(KeyError)
def keyerror_exception_handler(error):
    return render_template('keyerror.html')

@app.after_request
def after_request_func(response):
    path = request.path
    print(path)
    if (path != '/task/'):
        if(path != '/scripts/scripts.js'):
            if('/static/tmp/' not in path):
                print("after_request is running")
                directory = os.getcwd()+"/static/tmp/"
                filelist = [ f for f in os.listdir(directory)]
                for f in filelist:
                    if (f!='.gitkeep'):
                        os.remove(os.path.join(directory,f))
    return response
@app.errorhandler(NoTaskIDException)
def keyerror_exception_handler(error):
    return render_template('generalexception.html')

if __name__ == '__main__':
    app.run(debug=True)



