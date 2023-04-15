from util import qcards_db as db


class QCardsApp:

  def run(self):
    # Connect to the database
    qcardsDB = db.QCardsDB();
    cursor = qcardsDB.connect();

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print ("Database version : %s " % data)

qcards_app = QCardsApp();
qcards_app.run();
