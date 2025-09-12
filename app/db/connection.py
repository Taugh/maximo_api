# connection.py

import pyodbc
from config import SQL_SERVER, SQL_DATABASE, SQL_DRIVER, LDAP_USERNAME, LDAP_PASSWORD

class SQLServerConnection:
    def __init__(self):
        self.server = SQL_SERVER
        self.database = SQL_DATABASE
        self.driver = SQL_DRIVER
        self.username = LDAP_USERNAME
        self.password = LDAP_PASSWORD

    def get_connection(self):
        connection_string = (
            f"DRIVER={{{self.driver}}};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            f"UID={self.username};"
            f"PWD={self.password};"
            "Authentication=ActiveDirectoryPassword;"
        )
        try:
            return pyodbc.connect(connection_string)
        except pyodbc.Error as e:
            raise ConnectionError(f"Database connection failed: {e}")

    def get_cursor(self):
        conn = self.get_connection()
        return conn.cursor()


