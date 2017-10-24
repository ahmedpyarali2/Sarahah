# --- package imports
from functools import wraps

from sarahah import app
from sarahah.errors import InvalidUsage
from sarahah.utils import posted, get_token
from sarahah.users import current


def expects(parameters):
    """ A decorator that can allow us to validate the expected paramters of a request """
    
    def decorator(view_function):
        """ 
            Since we recived a list of parameters from our view function we need another
            decorator to pass on to the view function 
        """
        @wraps(view_function)
        def wrapper(*args, **kwargs):
            """ Wrapper function that validates parameters """

            # If no expecting any parameter
            if not parameters:
                return view_function({}, *args, **kwargs)

            # get request data in json form
            data = posted()

            # get valid recieved parameters
            received_params = {key : data.get(key) for key in parameters if data.get(key) not in [None, '']}

            # check if all expected paramters are recived or not
            if set(received_params.keys()) != set(parameters):
                raise InvalidUsage(message='Missing paramters: ' + ''.join(list(set(parameters) - set(received_params.keys()))), status_code=453)

            # return paramters back to the view function
            return view_function(received_params, *args, **kwargs)

        # retunr view function
        return wrapper

    return decorator


def authenticate(view_function):
    """ Check if user is logged in or not """

    @wraps(view_function)
    def wrapper(*args, **kwargs):
        request_token = get_token()
        user = current()

        if request_token != user['token']:
            raise InvalidUsage(message='Expired token', status_code=453)

        return view_function(*args, **kwargs)

    return wrapper