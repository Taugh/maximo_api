# db_connection.py

from connection import SQLServerConnection

def get_db_cursor():
    db = SQLServerConnection()
    conn = db.get_connection()
    return conn.cursor()
