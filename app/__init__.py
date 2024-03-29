from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for, blueprints
from config.config import Config
from services.DatabaseService import DatabaseService
from services.JSONEncoderService import ClassEncoder
from services.GradingService import GradingService
from werkzeug.utils import secure_filename
from models.Branch import Branch
from exceptions.NoTaskIDException import NoTaskIDException
import os
import sqlite3
from flask.helpers import url_for
class PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]


UPLOAD_FOLDER = '/app/static/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/grove')

# app.register_blueprint(bp, url_prefix='/grove')

database = DatabaseService()
grader = GradingService(database)

@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        shouldLogin = False
        for user in database.getUserCredentials():
            u = user._UserName
            p = user._UserPass
            if u.lower() == username.lower() and p == password:
                shouldLogin = True
            elif u.lower() == username.lower() and p != password:
                return render_template('index.html', loggedInUser="Incorrect password")

        if(shouldLogin):
            # add session persistance
            # This code assumes the user is a student
            userObject = [ele for ele in database.getUserCredentials(
            ) if ele.getUserName().lower() == username.lower() and ele.getUserPass() == password][0]
            if userObject.getUserType() == "Student":
                session['user_auth'] = ClassEncoder().encode(
                    database.getStudent(userObject.getUserID()))
                session['user_type'] = "STUDENT"
                return redirect(url_for('home'))
            elif userObject.getUserType() == "Teacher":
                session['user_auth'] = ClassEncoder().encode(
                    database.getTeacher(userObject.getUserID()))
                session['user_type'] = "TEACHER"
                return redirect(url_for('teacherconsole'))
        else:
            return render_template('index.html', loggedInUser="User does not exist")

    return render_template("index.html", loggedInUser="Please login below")

@app.errorhandler(KeyError)
def keyerror_exception_handler(error):
    return render_template('keyerror.html')

@app.after_request
def after_request_func(response):
    #print(os.getcwd())
    path = request.path
    #print(path)
    if (not path in ['/grove/task/', '/grove/scripts/scripts.js', '/grove/scripts/scripts.js', '/grove/static/css/global.css']):
        if '/static/tmp/' not in path:
            #print("after_request is running")
            directory = os.getcwd()+"/app/static/tmp/"
            filelist = [ f for f in os.listdir(directory)]
            for f in filelist:
                if (f!='.gitkeep'):
                    os.remove(os.path.join(directory,f))
    return response

@app.errorhandler(NoTaskIDException)
def keyerror_exception_handler(error):
    return render_template('generalexception.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


from app import task, projects, profile, home, classlist, logout, teacherconsole, award