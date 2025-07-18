import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='mindteck',
        cursorclass=pymysql.cursors.DictCursor
    )

def insert_contact(name, email, contactno, location, message):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO contact_details (Name, `Mobile Number`, `email id`, Location, message) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, contactno, email, location, message))
        conn.commit()
    finally:
        conn.close()