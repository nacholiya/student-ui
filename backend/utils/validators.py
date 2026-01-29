def validate_student_payload(data):
    required_fields = {
        "name": str,
        "age": int,
        "qualification": str,
        "graduation_year": int,
        "address": str,
        "email": str
    }

    if not isinstance(data, dict):
        return False, "Invalid JSON payload"

    for field, field_type in required_fields.items():
        if field not in data:
            return False, f"Missing field: {field}"

        if not isinstance(data[field], field_type):
            return False, f"Invalid type for field: {field}"

    return True, None
