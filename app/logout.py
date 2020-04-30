from config.config import Config
from app import app, database

@app.route('/logout')
def logout():
    session.pop('user_auth')
    return redirect('/')