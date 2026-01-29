from backend.utils.validators import validate_student_payload
from backend.utils.response import success_response, error_response
from flask import Blueprint, request, jsonify
from backend.services.student_service import create_student, fetch_students


students_bp = Blueprint("students", __name__)

@students_bp.route("/students", methods=["POST"])
def add_student():
    data = request.json

    is_valid, error = validate_student_payload(data)
    if not is_valid:
        return error_response(error, 400)

    try:
        create_student(data)
        return success_response(
            {"message": "Your data is saved successfully"},
            201
        )
    except Exception as e:
        print("DB ERROR:", e)
        return error_response(
            "Database is not connected. Data is not saved",
            500
        )


@students_bp.route("/students", methods=["GET"])
def get_students():
    try:
        students = fetch_students()
        return success_response(students, 200)
    except Exception as e:
        print("DB ERROR:", e)
        return error_response(
            "Failed to fetch students from database",
            500
        )
