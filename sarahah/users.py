""" Contains all user related functions """

# --- python imports
import uuid
from flask import jsonify

from sarahah import app
from sarahah.utils import get_token
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


def user_by_id(user_id):
    """ Gets the user form user id """
    sql = 'SELECT * from `user` WHERE `user_id`=%s'
    
    return db_read(sql, (user_id))


def get_user_session(user):

    token = '{0}'.format(uuid.uuid4())
    sql = 'UPDATE `user` SET `token` = %s WHERE `user_id` = %s'
    exception = db_insert(sql, (token, user['user_id']))

    if exception:
        return None
    return token


def current():
    """ Gets the currently logged in user """
    token = get_token()
    if token:
        sql = 'SELECT * FROM `user` WHERE `token` = %s'
        user = db_read(sql, (token))
        return user

    return None


def fetch_my_messages(user_id, inbox=True):
    """ Gets all the message for users """


    if inbox:
        sql = 'SELECT * FROM `message` WHERE `to_id` = %s'
    else:
        sql = 'SELECT * FROM `message` WHERE `from_id` = %s'
    
    messages = db_read(sql, (user_id))
    return messages


def send_anonymous(to, frm, message):
    """ Sends an anonymous message to a user """

    if not message:
        message = ''
    sql = 'INSERT INTO `message` (`m_id`, `to_id`, `from_id`, `message`) VALUES (%s, %s, %s, %s)'
    return db_insert(sql, ('{0}'.format(uuid.uuid4()), to, frm, message))