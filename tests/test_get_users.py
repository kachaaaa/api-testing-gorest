import requests
from utils.config import BASE_URL

def test_get_users_success():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_users_non_numeric_page():
    response = requests.get(f"{BASE_URL}/users", params={"page": "abc"})
    assert response.status_code in [200, 400, 422]

def test_get_users_negative_page():
    response = requests.get(f"{BASE_URL}/users", params={"page": -1})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_users_large_page():
    response = requests.get(f"{BASE_URL}/users", params={"page": 9999})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
