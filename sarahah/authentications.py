# --- package imports
from functools import wraps

from sarahah import app
from sarahah.errors import InvalidUsage
from sarahah.utils import posted


def expects(parameters):

    def decorator(view_function):

        @wraps(view_function)
        def wrapper(*args, **kwargs):

            if not parameters:
                return view_function({}, *args, **kwargs)

            data = posted()
            received_params = {key : data.get(key) for key in parameters if data.get(key) not in [None, '']}

            if set(received_params.keys()) != set(parameters):
                raise InvalidUsage(message='Missing paramters: ' + ''.join(list(set(parameters) - set(received_params.keys()))))

            return view_function(received_params, *args, **kwargs)

        return wrapper

    return decorator