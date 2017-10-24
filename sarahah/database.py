# ---  package imports
import uuid

from sarahah.config.config import DB_URL, DB_NAME

# --- pymysql import
import pymysql
import pymysql.cursors


def db_connect(host=DB_URL, user='root', password='1234'):
    """ Opens a connection to the database and returns the connection object """

    connection = None
    try:
        connection = pymysql.connect(host=host, user=user, password=password, db=DB_NAME, cursorclass=pymysql.cursors.DictCursor)

    except:
        pass

    return connection


def db_read(query, values=None):
    """ Performs the select query on the database """
    
    results = None
    connection = db_connect()
    if connection:
        with connection.cursor() as cursor:

            # execute the query
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)

            results = cursor.fetchall()

        connection.close()

    if len(results) == 0:
        return None

    if len(results) > 1:
        return results

    return results[0]




def db_insert(query, values=None):
    """ Performs the insert and update query on the database """

    # any excepton accoured
    exception = False

    connection = db_connect()
    if connection:
        try:
            with connection.cursor() as cursor:

                # execute the query
                if values:
                    cursor.execute(query, values)
                else:
                    cursor.execute(query)

            # commit the changes to database
            connection.commit()

        except pymysql.InternalError as error:

            # some exception happened.
            exception = True
            print(error.args[1])

        # close the connection to db adn return
        connection.close()
        return exception

    # cannot create a connection
    return True
