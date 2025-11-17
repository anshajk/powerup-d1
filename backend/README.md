# Telecom Device API (FastAPI)

A simple FastAPI backend that serves telecom/network device information from a static in-memory mock database.

## Features
- List all devices
- Filter devices by location using query parameter `location`
- Retrieve a single device by hostname

## Mock Database
```
MOCK_DEVICE_DB = {
    "router-blr-01": {"ip": "10.1.1.1", "vendor": "Cisco", "location": "Bengaluru"},
    "switch-swe-01": {"ip": "10.2.1.1", "vendor": "Juniper", "location": "Sweden"},
    "router-dub-01": {"ip": "10.3.1.1", "vendor": "Cisco", "location": "Dubai"},
}
```

## Project Structure
```
backend/
  app/
    main.py
    db/mock_devices.py
    models/device.py
    routers/devices.py
  tests/
    test_devices.py
  requirements.txt
```

## Installation
Make sure you are inside the `backend` directory and have a Python virtual environment active.

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

## Running the Server
```bash
uvicorn app.main:app --reload
```
Server will be available at: http://127.0.0.1:8000

## API Endpoints
### Health / Root
GET `/` -> `{ "message": "Telecom Device API - OK" }`

### Get Device
GET `/devices/{hostname}`
Returns 404 if the device does not exist.

### List Devices (optionally filtered)
GET `/devices/` — Returns all devices.
GET `/devices/?location=Bengaluru` — Returns devices whose `location` matches the query value exactly.

## Example Responses
`GET /devices/router-blr-01`
```json
{
  "hostname": "router-blr-01",
  "ip": "10.1.1.1",
  "vendor": "Cisco",
  "location": "Bengaluru"
}
```

`GET /devices/?location=Bengaluru`
```json
[
  {
    "hostname": "router-blr-01",
    "ip": "10.1.1.1",
    "vendor": "Cisco",
    "location": "Bengaluru"
  }
]
```

## Running Tests
From the `backend` directory:
```bash
pytest -q
```

## Next Improvements (Optional)
- Add pagination for large device lists
- Add vendor-based filtering
- Add dependency injection and configuration settings
- Replace mock DB with real database or external source

## License
MIT (sample project)
