import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["message"].startswith("Telecom Device API")


def test_get_device_success():
    r = client.get("/devices/router-blr-01")
    assert r.status_code == 200
    data = r.json()
    assert data["hostname"] == "router-blr-01"
    assert data["ip"] == "10.1.1.1"


def test_get_device_not_found():
    r = client.get("/devices/not-exist-01")
    assert r.status_code == 404
    assert r.json()["detail"] == "Device not found"


def test_list_devices_all():
    r = client.get("/devices/")
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 3


def test_list_devices_filter_location():
    r = client.get("/devices/?location=Bengaluru")
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 1
    assert data[0]["location"] == "Bengaluru"
