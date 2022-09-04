from config.config import Config
from app import app, database
from flask import session, redirect

@app.route('/logout')
def logout():
    session.pop('user_auth')
    return redirect('/grove')