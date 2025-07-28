import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('database.db')
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn


def create_table(conn):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS readmission (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER NOT NULL,
        readmitted INTEGER NOT NULL,
        feature1 REAL,
        feature2 REAL,
        feature3 REAL,
        ...
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def insert_data(conn, data):
    insert_sql = """
    INSERT INTO readmission (patient_id, readmitted, feature1, feature2, feature3, ...)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    try:
        cursor = conn.cursor()
        cursor.execute(insert_sql, data)
        conn.commit()
        print("Data inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")