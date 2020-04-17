import sqlite3
from models.Student import Student
from models.Teacher import Teacher
from models.Project import Project
from models.UserCredentials import UserCredentials
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

    def close_connection(self, exception):
        self._db.close()