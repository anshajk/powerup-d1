from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ip_private_10():
    r = client.get("/ip-utils/10.0.0.1/type")
    assert r.status_code == 200
    assert r.json() == {"ip": "10.0.0.1", "type": "Private"}


def test_ip_private_192_168():
    r = client.get("/ip-utils/192.168.1.77/type")
    assert r.status_code == 200
    assert r.json()["type"] == "Private"


def test_ip_public_example():
    r = client.get("/ip-utils/8.8.8.8/type")
    assert r.status_code == 200
    assert r.json() == {"ip": "8.8.8.8", "type": "Public"}
