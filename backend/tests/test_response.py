from backend.utils.response import success_response, error_response


def test_success_response_default_status():
    data = {"key": "value"}

    response, status_code = success_response(data)

    assert status_code == 200
    assert response["success"] is True
    assert response["data"] == data


def test_success_response_custom_status():
    response, status_code = success_response({"msg": "created"}, 201)

    assert status_code == 201
    assert response["success"] is True
    assert response["data"]["msg"] == "created"


def test_error_response_default_status():
    response, status_code = error_response("Something went wrong")

    assert status_code == 400
    assert response["success"] is False
    assert response["error"] == "Something went wrong"


def test_error_response_custom_status():
    response, status_code = error_response("DB error", 500)

    assert status_code == 500
    assert response["success"] is False
    assert response["error"] == "DB error"
