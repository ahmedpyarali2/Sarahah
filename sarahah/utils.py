# --- python imports
from flask import request

from sarahah import app


def posted():
    """ Returns request data in a python dict format """
    return request.get_json(force=True, silent=True) or {}


def get_token():
    """ Gets current token from request """
    return request.headers.get('X-Auth-Token', None)
