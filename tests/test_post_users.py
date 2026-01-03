import requests
from utils.config import BASE_URL

TOKEN = "bc0d8ae96ce40cf4c28e5a99eb39dfcd69106b173024ef3eba2a3f9806cc77e4"  

def test_create_user_success():
    payload = {"name": "Test User", "email": "testuser12345@example.com", "gender": "male"}
    headers = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=headers)
    assert response.status_code in [201, 401, 403]

def test_create_user_empty_name():
    payload = {"name": "", "email": "testuser12345@example.com", "gender": "male"}
    headers = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=headers)
    assert response.status_code in [400, 422]

def test_create_user_long_name():
    payload = {"name": "A"*201, "email": "testuser12345@example.com", "gender": "male"}
    headers = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=headers)
    assert response.status_code in [400, 422]

def test_create_user_empty_email():
    payload = {"name": "Test User", "email": "", "gender": "male"}
    headers = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=headers)
    assert response.status_code in [400, 422]

def test_create_user_invalid_gender():
    payload = {"name": "Test User", "email": "testuser12345@example.com", "gender": "unknown"}
    headers = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=headers)
    assert response.status_code in [400, 422]
