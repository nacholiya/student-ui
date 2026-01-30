from backend.db.connection import get_db_connection
from backend.db.exceptions import DatabaseError


def create_student(data):
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO students
            (name, age, qualification, graduation_year, address, email)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            data["name"],
            data["age"],
            data["qualification"],
            data["graduation_year"],
            data["address"],
            data["email"]
        ))

        conn.commit()

    except Exception as e:
        raise DatabaseError("Failed to create student") from e

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def fetch_students():
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

    except Exception as e:
        raise DatabaseError("Failed to fetch students") from e

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
