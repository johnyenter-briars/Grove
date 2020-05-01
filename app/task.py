from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database
from exceptions.NoTaskIDException import NoTaskIDException
from werkzeug.utils import secure_filename
from models.Branch import Branch

UPLOAD_FOLDER = '/app/static/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

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