from flask import Flask
from flask import request, redirect
from flask import render_template
from services.DatabaseService import DatabaseService

app = Flask(__name__)
database = DatabaseService()


@app.route('/')
def hello():
    # print(database.getStudents())
    return render_template("index.html", appName="The Grove", students=database.getStudents())


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


if __name__ == '__main__':
    app.run()
