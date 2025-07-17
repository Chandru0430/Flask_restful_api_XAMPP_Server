import pymysql

def get_db_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="mindtech",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def insert_contact(name, email, message):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, message))
        conn.commit()
    finally:
        conn.close()