import mysql.connector

class DbConectore:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="eagleeyedb"
        )


    def get_conection(self):
        return self.conn.cursor(dictionary=True)

    def close_conection(self):
        self.conn.cursor.close()
        self.conn.close()