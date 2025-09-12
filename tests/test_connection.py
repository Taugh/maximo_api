from app.db.connection import SQLServerConnection

def test_ldap_connection():
    try:
        db = SQLServerConnection()
        cursor = db.get_cursor()
        cursor.execute("SELECT GETDATE()")
        result = cursor.fetchone()
        print("✅ LDAP connection successful. Server time:", result[0])
    except Exception as e:
        print("❌ LDAP connection failed:", str(e))

if __name__ == "__main__":
    test_ldap_connection()
