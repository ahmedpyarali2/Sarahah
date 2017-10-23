# ---  package imports
import uuid
from flask import jsonify

from sarahah import app
from sarahah.authentications import expects
from sarahah.users import create, user_by_username, get_user_session
from sarahah.errors import InvalidUsage
from sarahah.utils import posted


# --- main views
@app.route('/')
def hello_world():
    """ basic hello world view """
    return 'Hello World'


@app.route('/register', methods=['POST'])
@expects(['username', 'password'])
def register(data):
    """ registers a user by adding there record to database """

    params = posted()
    username = params['username']
    password = params['password']

    uid = create(username, password)

    if not uid:
        raise InvalidUsage(message='Exception while creating user.', status_code=453)

    return jsonify(user_id=uid)


@app.route('/login', methods=['POST'])
@expects(['username', 'password'])
def login(data):
    """ creates a new session for the user """
    params = posted()
    username = params['username']
    password = params['password']

    user = user_by_username(username)

    if not user:
        raise InvalidUsage(message='User does not exist.', status_code=453)


    token = get_user_session(user)
    if not token:
        raise InvalidUsage(message='Cannot create a new session for current user.', status_code=453)
    
    return jsonify(token=token)




    