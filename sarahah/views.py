# ---  package imports
from sarahah import app


# --- main views

@app.route('/')
def hello_world():
    """ basic hello world view """
    return 'Hello World'