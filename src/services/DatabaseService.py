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
                .fetchall()]

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

    def getTasksForBranch(self, BranchID):
        return [Task(tuple) for tuple in self._db.execute("""
                    select * from Task where BranchID={id};""".format(id=BranchID)).fetchall()]

    def getAwardsForStudent(self, StudentID):
        return [Award(tuple) for tuple in self._db.execute(
            """select * from Award where StudentID={id};""".format(id=StudentID)).fetchall()]

    def getClassList(self, TeacherID):
        return [Student(tuple) for tuple in self._db.execute(
                """select * from Student where TeacherID={id};""".format(id=TeacherID)).fetchall()]

    def getProject(self, ProjectID):
        return [Project(tuple) for tuple in self._db.execute("""
            select * from Project where ProjectID={id}"""
            .format(id=ProjectID)).fetchall()][0]

    def getFilesForTask(self, FileID):
        return [Files(tuple) for tuple in self._db.execute("select * from Files;").fetchall()] 

    def convertToBinaryData(self,FileName):
        #Convert digital data to binary format
        with open(FileName, 'rb') as file:
            blobData = file.read()
        return blobData

    def insertBLOB(self, FileID, FileName, FileType):
        try:
            self._db.execute(""" INSERT INTO new_employee
            (FileID, FileName, FileType) VALUES (?, ?, ?)""", (FileID, FileName, FileType))
            self._db.commit()
        except sqlite3.Error as error:
            print("Failed to insert blob data into sqlite table", error)

    def close_connection(self, exception):
        self._db.close()
        