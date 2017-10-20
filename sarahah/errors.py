# --- python imports
from flask import jsonify

from sarahah import app


class InvalidUsage(Exception):
    """ Custom exception implementation to raise on any invalid usage inside the api """
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code:
            self.status_code = status_code

        self.payload = payload

    def to_dict(self):
        """ Allows exception to be converted to dictionary. """
        response = dict(self.payload or ())
        response['message'] = self.message
        response['status_code'] = self.status_code
        return response


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    """ Global handler for InvalidUsage exception. """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response