from flask import Blueprint, request, jsonify
from backend.services.student_service import create_student, fetch_students


students_bp = Blueprint("students", __name__)

@students_bp.route("/students", methods=["POST"])
def add_student():
    try:
        create_student(request.json)
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

@students_bp.route("/students", methods=["GET"])
def get_students():
    try:
        return jsonify(fetch_students()), 200
    except Exception as e:
        print("DB ERROR:", e)
        return jsonify([]), 200   # keep frontend behavior unchanged
