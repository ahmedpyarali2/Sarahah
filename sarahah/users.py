""" Contains all user related functions """

# --- python imports
import uuid
from flask import jsonify

from sarahah import app
from sarahah.database import db_insert


def create(username, password):
    """ Creats a new user and writes to the database """

    # generate a user token
    uid = '{0}'.format(uuid.uuid4())
    token = ''
    sql = 'INSERT INTO `user` (`user_id`, `username`, `password`, `token`) VALUES (%s, %s, %s, %s)'
    exception = db_insert(sql, (uid, username, password, token))

    if exception:
        return None

    return uid