# Telecom Device API (FastAPI)

A simple FastAPI backend that serves telecom/network device information from a static in-memory mock database and provides an IP classification utility.

## Features
- List all devices
- Filter devices by location using query parameter `location`
- Retrieve a single device by hostname
- Classify an IP as Private or Public

## Mock Database
```
MOCK_DEVICE_DB = {
    "router-blr-01": {"ip": "10.1.1.1", "vendor": "Cisco", "location": "Bengaluru"},
    "switch-mum-01": {"ip": "10.2.1.1", "vendor": "Juniper", "location": "Sweden"},
    "router-del-01": {"ip": "10.3.1.1", "vendor": "Cisco", "location": "Dubai"},
}
```

## Project Structure
```
backend/
  app/
    main.py
    db/mock_devices.py
    models/
      device.py
      ip_utils.py
    routers/
      devices.py
      ip_utils.py
  tests/
    test_devices.py
    test_ip_utils.py
  requirements.txt
```

## Installation
From `backend` directory:
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

## Running the Server
```bash
uvicorn app.main:app --reload
```
Server: http://127.0.0.1:8000

## API Endpoints
### Root
GET `/` → Health/status

### Devices
GET `/devices/` — List all devices
GET `/devices/?location=Bengaluru` — Filter by location
GET `/devices/{hostname}` — Get single device (404 if missing)

### IP Classification
GET `/ip-utils/{ip_address}/type` — Returns whether the IP is `Private` or `Public`.
Logic (simplified):
```python
if ip_address.startswith("10.") or ip_address.startswith("192.168."):
    ip_type = "Private"
else:
    ip_type = "Public"
```
Example:
```bash
curl http://127.0.0.1:8000/ip-utils/10.0.0.9/type
# {"ip":"10.0.0.9","type":"Private"}
```

## Running Tests
```bash
pytest -q
```

## Future Enhancements
- Add 172.16.0.0/12 private range detection
- CIDR parsing for more accurate classification
- Vendor or location creation endpoints (requires persistence layer)
- Logging & metrics middleware

## License
MIT (sample project)
