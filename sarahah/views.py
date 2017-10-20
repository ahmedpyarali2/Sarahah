# ---  package imports
import uuid
from flask import jsonify

from sarahah import app
from sarahah.authentications import expects


# --- main views
@app.route('/')
def hello_world():
    """ basic hello world view """
    return 'Hello World'


@app.route('/register', methods=['POST'])
@expects(['username', 'password'])
def register(data):
    """ registers a user by adding there record to database """

    user = {
        'token' : '{0}'.format(uuid.uuid4()),
        'id' : '{0}'.format(uuid.uuid4())
    }

    return jsonify(user)


    