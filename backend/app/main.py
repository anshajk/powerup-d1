from fastapi import FastAPI
from app.routers import devices, ip_utils

app = FastAPI(title="Telecom Device API", version="1.0.0")

app.include_router(devices.router)
app.include_router(ip_utils.router)


@app.get("/")
async def root():
    return {"message": "Telecom Device API - OK"}
