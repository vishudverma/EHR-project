import pyodbc

def test_connection():
    """Test connection to SQL Server using Windows Authentication"""
    conn_str = (
        r"DRIVER={ODBC Driver 17 for SQL Server};"
        r"SERVER=VISHUD_LAPTOP\SQLEXPRESS;"
        r"DATABASE=ehr_readmission;"
        r"Trusted_Connection=yes;"
    )
    
    try:
        conn = pyodbc.connect(conn_str)
        print("Successfully connected to the database!")
        
        # Get server version to verify connection
        cursor = conn.cursor()
        cursor.execute("SELECT @@VERSION")
        version = cursor.fetchone()[0] # type: ignore
        print(f"\nSQL Server Version:\n{version}")
        
        cursor.close()
        conn.close()
        return True
    except pyodbc.Error as e:
        print(f"Failed to connect to the database.")
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_connection()
