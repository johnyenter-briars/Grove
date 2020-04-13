import sqlite3
from flask import g

DATABASE = 'database_files/Grove.db'

class DatabaseService(object):

    def __init__(self):
        super().__init__()
        self.get_db()
        self._db = None


    def set_db(self):
        self._db = getattr(g, '_database', None)
        if self._db is None:
            self._db = g._database = sqlite3.connect(DATABASE)
        return self._db

    def get_db(self):
        return self._db

    @app.teardown_appcontext
    def close_connection(self, exception):
        self._db = getattr(g, '_database', None)
        if self._db is not None:
            self._db.close()