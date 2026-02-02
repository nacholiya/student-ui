from backend.utils.validators import validate_student_payload


def test_valid_student_payload():
    payload = {
        "name": "Test User",
        "age": 22,
        "qualification": "BSc",
        "graduation_year": 2024,
        "address": "India",
        "email": "test@example.com"
    }

    is_valid, error = validate_student_payload(payload)

    assert is_valid is True
    assert error is None


def test_missing_field_in_payload():
    payload = {
        "name": "Test User",
        "age": 22
    }

    is_valid, error = validate_student_payload(payload)

    assert is_valid is False
    assert error == "Missing field: qualification"


def test_invalid_type_in_payload():
    payload = {
        "name": "Test User",
        "age": "twenty",
        "qualification": "BSc",
        "graduation_year": 2024,
        "address": "India",
        "email": "test@example.com"
    }

    is_valid, error = validate_student_payload(payload)

    assert is_valid is False
    assert error == "Invalid type for field: age"
