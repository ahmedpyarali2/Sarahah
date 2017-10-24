# ---  package imports
import uuid
from flask import jsonify

from sarahah import app
from sarahah.authentications import expects, authenticate
from sarahah.users import create, user_by_username, get_user_session, current, fetch_my_messages
from sarahah.users import send_anonymous, user_by_id
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


@app.route('/me/inbox', methods=['GET'])
@authenticate
def my_inbox():
    """ fetches inbox messages for currently logged in user """
    user = current()

    if not user:
        raise InvalidUsage(messages='Invalid user.', status_code=453)


    messages = fetch_my_messages(user['user_id'])

    if not messages:
        messages = []

    return jsonify(messsages=messages)


@app.route('/me/outbox', methods=['GET'])
@authenticate
def my_outbox():
    """ fetches outbox messages for currently logged in user """
    user = current()

    if not user:
        raise InvalidUsage(messages='Invalid user.', status_code=453)


    messages = fetch_my_messages(user['user_id'], inbox=False)

    if not messages:
        messages = []

    return jsonify(messsages=messages)


@app.route('/message', methods=['POST'])
@expects(['to_id', 'message'])
@authenticate
def send(data):
    """ Send an anonymous message to a user """
    sender = current()
    receiver = user_by_id(data['to_id'])

    if not sender:
        raise InvalidUsage(messages='Invalid user.', status_code=453)

    if not receiver:
        raise InvalidUsage(messages='This user is not registered yet.', status_code=453)


    if not send_anonymous(receiver['user_id'], sender['user_id'], data['message']):
        return jsonify(status='OK')

    raise InvalidUsage(message='Error while writing message', status_code=453)







    