import pytest
from utils.api_client import APIClient

client = APIClient()
BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.api
def test_get_post():
    response = client.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


@pytest.mark.api
def test_create_post():
    payload = {
        "title": "Demo",
        "body": "API Testing",
        "userId": 1
    }
    response = client.post(f"{BASE_URL}/posts", payload)
    assert response.status_code == 201


@pytest.mark.api
def test_update_post():
    payload = {
        "title": "Updated",
        "body": "Updated Body",
        "userId": 1
    }
    response = client.put(f"{BASE_URL}/posts/1", payload)
    assert response.status_code == 200


@pytest.mark.api
def test_delete_post():
    response = client.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200