import json
from unittest.mock import patch
from backend.app import create_app


def test_get_students_success():
    app = create_app()
    client = app.test_client()

    with patch("backend.routes.students.fetch_students") as mock_fetch:
        mock_fetch.return_value = [
            {"id": 1, "name": "Test User"}
        ]

        response = client.get("/students")

        data = json.loads(response.data)

        assert response.status_code == 200
        assert data["success"] is True
        assert len(data["data"]) == 1


def test_get_students_db_failure():
    app = create_app()
    client = app.test_client()

    with patch("backend.routes.students.fetch_students") as mock_fetch:
        mock_fetch.side_effect = Exception("DB down")

        response = client.get("/students")
        data = json.loads(response.data)

        assert response.status_code == 500
        assert data["success"] is False
        assert "Failed to fetch students" in data["error"]


def test_create_student_validation_failure():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/students",
        json={"name": "OnlyName"}
    )

    data = json.loads(response.data)

    assert response.status_code == 400
    assert data["success"] is False
    assert "Missing field" in data["error"]


def test_create_student_success():
    app = create_app()
    client = app.test_client()

    payload = {
        "name": "Test User",
        "age": 22,
        "qualification": "BSc",
        "graduation_year": 2024,
        "address": "India",
        "email": "test@example.com"
    }

    with patch("backend.routes.students.create_student") as mock_create:
        response = client.post("/students", json=payload)
        data = json.loads(response.data)

        assert response.status_code == 201
        assert data["success"] is True
        mock_create.assert_called_once()
