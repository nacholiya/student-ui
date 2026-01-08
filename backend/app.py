from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# ---------- DB CONFIG (ENV VARS) ----------
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "auth_plugin": "mysql_native_password"
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# ---------- HEALTH ----------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "backend running"}), 200

# ---------- CREATE STUDENT ----------
@app.route("/students", methods=["POST"])
def create_student():
    data = request.json

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO students (name, age, qualification, graduation_year, address, email)
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
        cursor.close()
        conn.close()

        return jsonify({
            "status": "success",
            "message": "Your data is saved successfully"
        }), 201

    except Exception as e:
        print("DB ERROR:", e)
        return jsonify({
            "status": "error",
            "message": "Database is not connected. Data is not saved"
        }), 500

# ---------- GET STUDENTS ----------
@app.route("/students", methods=["GET"])
def get_students():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(students), 200

    except Exception as e:
        print("DB ERROR:", e)
        return jsonify([]), 200   # frontend shows empty list

if __name__ == "__main__":
    app.run(port=5001, debug=False)
