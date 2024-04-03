import pytest
from src.app import flask_app
from flask import json

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        with flask_app.app_context():
            # Perform any necessary setup for testing
            yield client

def test_user_create(client):
    # Define your test data
    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "gender": "Male",
        "phone_number": "1234567890"
    }

    # Make a POST request to create a user
    response = client.post('/users', json=user_data)
    assert response.status_code == 201

    # Validate the response or perform additional checks as needed
    data = json.loads(response.data)
    assert 'message' in data

    # Add more test cases as needed

def test_user_update(client):
    # Define your test data and make a PUT request to update a user
    pass

def test_user_delete(client):
    # Define your test data and make a DELETE request to delete a user
    pass

if __name__ == "__main__":
    pytest.main()
