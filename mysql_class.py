import os
import mysql.connector


def handle_exceptions(f):
    def wrapper(*args, **kw):
        try:
            return f(*args, **kw)
        except Exception as e :
            print(f"Error with details {e}")
            return False
    return wrapper


class MySQl:
    host = os.environ["DB_HOST"]
    port = os.environ["DB_PORT"]
    username = os.environ["DB_USERNAME"]
    password = os.environ["DB_PASSWORD"]

    def connect(self):
        try:
            connection = mysql.connector.connect(host=self.host,
                                               user=self.username,
                                               password=self.password)

            return connection
        except Exception as e:
            print("Error while connecting to MySQL", e)
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")

    @handle_exceptions
    def execute_statement(self, statement, multi=False):
        connection = self.connect()
        cursor = connection.cursor()
        res = cursor.execute(statement, multi=multi)
        connection.commit()
        connection.close()
        return res
