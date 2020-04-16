import sqlite3

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

    def getStudents(self):
        return self._db.execute("select * from Student;").fetchall()

    def close_connection(self, exception):
        self._db.close()