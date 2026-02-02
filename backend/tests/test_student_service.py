import pytest
from unittest.mock import MagicMock, patch

from backend.services.student_service import fetch_students, create_student
from backend.db.exceptions import DatabaseError


@patch("backend.services.student_service.get_db_connection")
def test_fetch_students_success(mock_get_db_connection):
    # Mock cursor
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        {"id": 1, "name": "Test User"}
    ]

    # Mock connection
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    mock_get_db_connection.return_value = mock_conn

    students = fetch_students()

    assert students == [{"id": 1, "name": "Test User"}]
    mock_cursor.execute.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_conn.close.assert_called_once()


@patch("backend.services.student_service.get_db_connection")
def test_fetch_students_db_failure(mock_get_db_connection):
    mock_get_db_connection.side_effect = Exception("DB down")

    with pytest.raises(DatabaseError):
        fetch_students()


@patch("backend.services.student_service.get_db_connection")
def test_create_student_success(mock_get_db_connection):
    mock_cursor = MagicMock()
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    mock_get_db_connection.return_value = mock_conn

    payload = {
        "name": "Test User",
        "age": 22,
        "qualification": "BSc",
        "graduation_year": 2024,
        "address": "India",
        "email": "test@example.com"
    }

    create_student(payload)

    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_conn.close.assert_called_once()


@patch("backend.services.student_service.get_db_connection")
def test_create_student_db_failure(mock_get_db_connection):
    mock_get_db_connection.side_effect = Exception("DB down")

    payload = {
        "name": "Test User",
        "age": 22,
        "qualification": "BSc",
        "graduation_year": 2024,
        "address": "India",
        "email": "test@example.com"
    }

    with pytest.raises(DatabaseError):
        create_student(payload)
