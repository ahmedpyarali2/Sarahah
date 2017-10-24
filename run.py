""" This file needs to be run to start the server.
    For now we are just initalizing the app.
    We are going to use a virtualenv later.
""" 

# --- python imports
import os
import sys


def activate_venv():
    """ activates the virtual environment by calling the avtivate_this.py file """

    # construct virtual environment path.
    this = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(this, 'venv/bin/activate_this.py')

    # check if we can activate the virtual environment at standard location.
    if not os.path.isfile(path):
        print('[ERROR] Seems like you have not activated your virtual environment.')
        print('[ERROR] I tried to load from the standard location, but was not able to find it.')
        print('Please create a virtual environment at: {0}'.format('{0}/venv'.format(this)))
        sys.exit(1)

    # activate the virtual environment.
    execfile(path, dict(__file__=path))


def run_app():
    # import app
    from sarahah import app

    # run app
    app.run(debug=True)


if __name__ == '__main__':
    activate_venv()
    run_app()