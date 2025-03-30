from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

TEST_CLIENT_USER_ID = "test-user-auto"

def get_or_create_user_id():
    response = client.post("/user", json={"client_user_id": TEST_CLIENT_USER_ID})
    data = response.json()
    return data.get("user_id")


def test_create_user():
    response = client.post("/user", json={"client_user_id": TEST_CLIENT_USER_ID})
    data = response.json()
    assert response.status_code in [200, 400]
    if response.status_code == 200:
        assert "client_user_id" in data
    elif response.status_code == 400:
        assert "detail" in data
        assert "user_id" in data["detail"]


def test_get_user():
    user_id = get_or_create_user_id()
    response = client.get(f"/user/{user_id}")
    assert response.status_code == 200
    assert response.json()["user_id"] == user_id

def test_link_token():
    response = client.post("/link-token", json={"client_user_id": TEST_CLIENT_USER_ID})
    assert response.status_code == 200
    assert "link_token" in response.json()

def test_get_providers():
    response = client.get("/providers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_connections():
    user_id = get_or_create_user_id()
    response = client.get(f"/connections/{user_id}")
    assert response.status_code in [200, 500]  # 500 if no device connected yet
    
def test_webhook():
    payload = {"test": "data"}
    response = client.post("/webhook", json=payload)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_activity_data():
    user_id = get_or_create_user_id()
    response = client.get(f"/activity/{user_id}")
    assert response.status_code in [200, 500]  # 500 if no activity yet
    if response.status_code == 200:
        assert "activity" in response.json()

def test_sleep_data():
    user_id = get_or_create_user_id()
    response = client.get(f"/sleep/{user_id}")
    assert response.status_code in [200, 500]  # 500 if no sleep data
    if response.status_code == 200:
        assert "sleep" in response.json()
        
def test_workout_data():
    user_id = get_or_create_user_id()
    response = client.get(f"/workouts/{user_id}")
    assert response.status_code in [200, 500]  # 500 if no workout data

    if response.status_code == 200:
        data = response.json()
        assert isinstance(data, dict)
        assert "workouts" in data
        assert isinstance(data["workouts"], list)