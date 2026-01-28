from backend.db.connection import get_db_connection


def create_student(data):
    query = """
        INSERT INTO students
        (name, age, qualification, graduation_year, address, email)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(query, (
        data["name"],
        data["age"],
        data["qualification"],
        data["graduation_year"],
        data["address"],
        data["email"]
    ))

    conn.commit()
    cursor.close()
    conn.close()

def fetch_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students
