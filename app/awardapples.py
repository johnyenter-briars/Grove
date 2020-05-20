from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from app import app, database

@app.route('/awardapples')
def awardapples():
    sess = json.loads(session['user_auth'])
    if not sess:
        return redirect('/')
    first = sess.get('_FirstName')
    last = sess.get('_LastName')


    return render_template("awardapples.html")