# test_connection.py

from app.db.connection import SQLServerConnection

def test_windows_auth_connection():
    try:
        with SQLServerConnection() as conn:
            conn.raw_cursor.execute("SELECT GETDATE()")
            result = conn.raw_cursor.fetchone()
            if result is not None:
                print("✅ Windows Auth connection successful. Server time:", result[0])
            else:
                print("❌ Query returned no results.")
    except Exception as e:
        print("❌ Windows Auth connection failed:", str(e))

if __name__ == "__main__":
    test_windows_auth_connection()

