from enum import Enum
import MySQLdb as mysql

"""
Description: An enum to define database connection properties
Author: Jaco Koekemoer
Date: 29 March 2023
"""
class QCardsDB(Enum):

    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "password"
    DB_DATABASE = "qcards"

"""
Description: A class for getting a database connection
Author: Jaco Koekemoer
Date: 30 March 2023
"""
class QCardsDatabaseConnection:

    def __enter__(self):
        self.conn = mysql.connect(host=QCardsDB.DB_HOST.value,  # your host
                             user=QCardsDB.DB_USER.value,       # username
                             passwd=QCardsDB.DB_PASSWORD.value,     # password
                             db=QCardsDB.DB_DATABASE.value)   # name of the database
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

"""
Description: A class for executing database queries
Author: Jaco Koekemoer
Date: 30 March 2023
"""
class QCardsExecuteQuery:

    def execute(self, sql):
        # Connect to the database
        with QCardsDatabaseConnection() as conn:
            cursor = conn.cursor()

            try:
               # Execute the SQL command
               cursor.execute(sql)
               # Commit your changes in the database
               conn.commit()
            except Exception as e:
               # Rollback in case there is any error
               print ("An error occured, rolling back {:s}: {}".format(description, str(e)))
               conn.rollback()

"""
Description: A class for executing database select queries
Author: Jaco Koekemoer
Date: 30 March 2023
"""
class QCardsExecuteSelectQuery:

    def execute(self, sql):
        # Connect to the database
        with QCardsDatabaseConnection() as conn:
            cursor = conn.cursor()

            try:
               # Execute the SQL command
               cursor.execute(sql)
               # Fetch all
               return cursor.fetchall()
            except Exception as e:
               # Rollback in case there is any error
               print ("An error occured, rolling back {:s}: {}".format(description, str(e)))
               conn.rollback()
