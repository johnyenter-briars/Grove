from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from config import Config
from services.DatabaseService import DatabaseService
from services.JSONEncoderService import ClassEncoder
from werkzeug.utils import secure_filename
from models.Branch import Branch
import os
from flask.helpers import url_for
UPLOAD_FOLDER = '/static/img'
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

    for branch in branches:
        for studentId in branch.getStudents():
            studentsOnProject[studentId] = database.getStudent(studentId)
        
    return render_template("projects.html", name=first+' '+last, 
        teach=teacherObj.getFirstName() + " " + teacherObj.getLastName(), 
        proj=projectObj, 
        perm=perm,
        branches=branches,
        studentsOnProject=studentsOnProject)

@app.route('/task', methods=['POST', 'GET'])
def task():
    #NOT COMPLETE - Unable to make a post call (changed span to button but it still didn't work)
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['fileType']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    # This is code to check if the "file" from the database can be returned
    files = database.getFilesForTask(1)[0]
    displayPhoto = files.getPhoto()
    sess = json.loads(session['user_auth'])
    first = sess.get('_FirstName')
    last = sess.get('_LastName')
    return render_template("task.html", name=first+' '+last, displayPhoto=displayPhoto)

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
    
    return render_template("classlist.html", students=students)

@app.errorhandler(KeyError)
def keyerror_exception_handler(error):
    return render_template('keyerror.html')

if __name__ == '__main__':
    app.run(debug=True)



