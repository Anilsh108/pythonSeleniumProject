import requests

def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200

    json_data = response.json()
    assert json_data["userId"] == 1
    assert json_data["id"] == 1

    #driver--code python selenium script