# connection.py

import pyodbc
from app.config import SQL_SERVER, SQL_DATABASE, SQL_DRIVER
from typing import Optional

class SQLServerConnection:
    def __init__(self):
        self.connection_string = (
            f"DRIVER={{{SQL_DRIVER}}};"
            f"SERVER={SQL_SERVER};"
            f"DATABASE={SQL_DATABASE};"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )
        self.conn = None
        self.cursor = None

    def __enter__(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            self.cursor = self.conn.cursor()
            return self
        except pyodbc.Error as e:
            raise ConnectionError(f"Database connection failed: {e}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    @property
    def raw_cursor(self):
        if self.cursor is None:
            raise RuntimeError("Cursor is not initialized.")
        return self.cursor

    def execute_query(self, query: str, params: Optional[tuple] = None):
        """
        Executes a SQL query. Supports parameterized queries.
        Returns all fetched rows.
        """
        if self.cursor is None:
            raise RuntimeError("Database cursor is not initialized. Use the context manager (with statement).")
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except pyodbc.Error as e:
            raise RuntimeError(f"Query execution failed: {e}")




