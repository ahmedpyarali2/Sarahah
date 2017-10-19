""" This file needs to be run to start the server.
	For now we are just initalizing the app.
	We are going to use a virtualenv later.
""" 


def run_app():
	# import app
	from sarahah import app

	# run app
	app.run(debug=True)


if __name__ == '__main__':
	run_app()