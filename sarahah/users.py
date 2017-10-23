""" Contains all user related functions """

# --- python imports
import uuid
from flask import jsonify

from sarahah import app
from sarahah.database import db_read, db_insert


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

def user_by_username(username):
    """ Get the user from username """

    sql = 'SELECT * from `user` WHERE `username`=%s'
    
    return db_read(sql, (username))


def get_user_session(user):

    token = '{0}'.format(uuid.uuid4())
    sql = 'UPDATE `user` SET `token` = %s WHERE `user_id` = %s'
    exception = db_insert(sql, (token, user['user_id']))

    if exception:
        return None
    return token