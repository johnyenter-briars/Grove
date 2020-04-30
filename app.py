# Run with: python[3] -m flask run
from app import app

@app.shell_context_processor
def make_shell_context():
    return None
