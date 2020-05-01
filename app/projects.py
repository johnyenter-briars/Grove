from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database

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