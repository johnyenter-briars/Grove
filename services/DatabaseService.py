import sqlite3
from models.Student import Student
from models.Teacher import Teacher
from models.Project import Project
from models.UserCredentials import UserCredentials
from models.Branch import Branch
from models.Award import Award
from services.FlattenerService import BranchFlattener
from models.Files import Files
from models.Task import Task
from models.Chat import Chat
from models.TaskReview import TaskReview
from models.Goal import Goal
import os

DATABASE_PATH = 'database_files/Grove.db'

class DatabaseService(object):

    def __init__(self):
        super().__init__()
        self._db = None
        self.set_db()

    def set_db(self):
        self._db = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        
    def get_db(self):
        return self._db

    def getUserCredentials(self):
        return [UserCredentials(tuple) for tuple in self._db.execute("select * from UserCredentials;").fetchall()] 

    def getStudents(self):
        return [Student(tuple) for tuple in self._db.execute("select * from Student;").fetchall()] 
    
    def getTeachers(self):
        return [Teacher(tuple) for tuple in self._db.execute("select * from Teacher;").fetchall()]

    def getStudentProject(self, StudentID):
         return [Project(tuple) for tuple in 
                self._db.execute("""select * from Project where ProjectID = 
                (select ProjectID from Student where StudentID = {id});""".format(id=StudentID))
                .fetchall()][0]

    def getStudent(self, StudentID):
        return [Student(tuple) for tuple in self._db.execute(
                """select * from Student where StudentID={id};""".format(id=StudentID)).fetchall()][0]

    def getTeacher(self, TeacherID):
        return [Teacher(tuple) for tuple in self._db.execute(
                """select * from Teacher where TeacherID={id};""".format(id=TeacherID)).fetchall()][0]
    
    def getBranchesForProject(self, ProjectID):
        return BranchFlattener(
                self._db.execute("""select * from Branch where ProjectID={id};"""
                .format(id=ProjectID)).fetchall()).flatten()
    
    def getBranchesForStudent(self, StudentID):
        return BranchFlattener(
                self._db.execute("""select * from Branch where StudentID={id};"""
                .format(id=StudentID)).fetchall()).flatten()

    def getTasksForBranch(self, BranchID, ProjectID):
        return [Task(tuple) for tuple in self._db.execute("""
                    select * from Task where BranchID={bid} and ProjectID={pid};"""
                    .format(bid=BranchID, pid=ProjectID)).fetchall()]

    def getAwardsForStudent(self, StudentID):
        return [Award(tuple) for tuple in self._db.execute(
            """select * from Award where StudentID={id};""".format(id=StudentID)).fetchall()]
    
    def getTasksForStudent(self, StudentID):
        return [Task(tuple) for tuple in self._db.execute(
            """select * from Task where StudentID={id};""".format(id=StudentID)).fetchall()]

    def getClassList(self, TeacherID):
        return [Student(tuple) for tuple in self._db.execute(
                """select * from Student where TeacherID={id};""".format(id=TeacherID)).fetchall()]

    def getProject(self, ProjectID):
        return [Project(tuple) for tuple in self._db.execute("""
            select * from Project where ProjectID={id}"""
            .format(id=ProjectID)).fetchall()][0]

    def getStudentsOnProject(self, ProjectID):
        return [Student(tuple) for tuple in self._db.execute("""
            select * from Student where ProjectID={id}"""
            .format(id=ProjectID)).fetchall()]


    def getProjects(self):
        return [Project(tuple) for tuple in self._db.execute("select * from Project").fetchall()]

    def addMessage(self, UserName, TaskID, TimeStamp, MessageString):
        self._db.execute(""" INSERT INTO Chat
            (UserName, TaskID, TimeStamp, MessageString) VALUES (?, ?, ?, ?)""", (UserName, TaskID, TimeStamp, MessageString))
        self._db.commit()

    def getChatForTask(self, TaskID):
        return [Chat(tuple) for tuple in self._db.execute(
                """select * from Chat where TaskID={id};""".format(id=TaskID)).fetchall()]

    def getTask(self, TaskID):
        return [Task(tuple) for tuple in self._db.execute("""
        select * from Task where TaskID={id};"""
        .format(id=TaskID)).fetchall()][0]

    def getGoalForProject(self, ProjectID):
        return [Goal(tuple) for tuple in self._db.execute("""
        select * from ProjectGoal where ProjectID = {id}"""
        .format(id=ProjectID)).fetchall()][0]

    def getFilesForTask(self, TaskID):
        return [Files(tuple) for tuple in self._db.execute(
                """select * from Files where TaskID={id};""".format(id=TaskID)).fetchall()]

    def addFile(self, TaskID, FileName, FileType):
        try:
            self._db.execute(""" INSERT INTO Files
            (TaskID, FileName, FileType) VALUES (?, ?, ?)""", (TaskID, FileName, FileType))
            self._db.commit()
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

    def removeFile(self, FileName):
        try:
            self._db.execute(""" DELETE FROM Files
            WHERE FileName = ?""", (FileName,))
            self._db.commit()
            
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
            
    def insertNewStudent(self, FirstName:str, LastName:str, TeacherID:int, ProjectID: int, PermissionLevel:str):
        try:
            self._db.execute("""insert into Student(FirstName, LastName, TeacherID, 
                                ProjectID, RoleType) 
                                values("{fname}", "{lname}", {teachID}, {projID}, "{permLvl}");"""
                                .format(fname=FirstName, lname=LastName, teachID=TeacherID,
                                        projID=ProjectID, permLvl=PermissionLevel))
            self._db.commit()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

    def insertNewTask(self, BranchID: int, StudentID: int, ProjectID: int, TaskDesc: str):
        try:
            self._db.execute("""insert into Task
                                (BranchID, StudentID, ProjectID, TaskDescription, Resolved)
                                values({bID}, {sID}, {pID}, "{tDesc}", 0);"""
                                .format(bID=BranchID, sID=StudentID, pID=ProjectID, tDesc=TaskDesc))
            self._db.commit()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

    def insertTaskReview(self, TaskID: int):
        try:
            self._db.execute("""insert into TaskReview
                                (TaskID, Resolved)
                                values({tID}, 0);"""
                                .format(tID=TaskID))
            self._db.commit()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

    def markTaskResolved(self, TaskID: int):
        try:
            self._db.execute("""UPDATE TaskReview
                                SET Resolved = 1
                                WHERE TaskID = {tID}"""
                                .format(tID=TaskID))
            self._db.commit()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

    def getTasksToBeReviewed(self):
        return [TaskReview(tuple) for tuple in self._db.execute("select * from TaskReview").fetchall()]


    def close_connection(self, exception):
        self._db.close()
        