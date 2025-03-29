# main.py
from fastapi import FastAPI, HTTPException, Request
from junction import create_user, generate_link_token, get_providers
from models import UserCreate, BiomarkerReading
from db import save_user_mapping, get_junction_user_id
from typing import List
from datetime import datetime

print("beginning of main.py")
app = FastAPI()

devices = {}
biomarker_data: List[BiomarkerReading] = []

@app.post("/user")
def create_user_route(user: UserCreate):
    try:
        print(f"[DEBUG] Attempting to create user: {user.client_user_id}")
        response = create_user(user.client_user_id)
        junction_user_id = response["id"]
        # save_user_mapping(user.client_user_id, junction_user_id)
        return {"oktaUserId": user.client_user_id, "junctionUserId": junction_user_id}
    except Exception as e:
        print("Error in /user route:", e)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test")
def test_route():
    return {"message": "test route works"}

@app.get("/link-token/{okta_user_id}")
async def get_link_token(okta_user_id: str):
    junction_user_id = get_junction_user_id(okta_user_id)
    print(f"[DEBUG] okta_user_id={okta_user_id}, junction_user_id={junction_user_id}")
    if not junction_user_id:
        raise HTTPException(status_code=404, detail="User not found")
    return generate_link_token(junction_user_id)

@app.post("/device/{provider}/reconnect")
async def reconnect_device(provider: str):
    return {"status": "reconnect flow triggered", "provider": provider}

@app.delete("/device/{provider}")
async def revoke_device(provider: str):
    devices.pop(provider, None)
    return {"status": "revoked", "provider": provider}

@app.post("/webhook")
async def receive_webhook(request: Request):
    payload = await request.json()
    # storing example biomarker reading
    if "junctionUserId" in payload and "type" in payload:
        biomarker_data.append(BiomarkerReading(
            junctionUserId=payload["junctionUserId"],
            type=payload["type"],
            timestamp=datetime.utcnow(),
            minRange=payload.get("minRange", 0),
            maxRange=payload.get("maxRange", 100),
        ))
    return {"status": "received"}

@app.get("/data/{okta_user_id}")
async def get_health_data(okta_user_id: str):
    junction_user_id = get_junction_user_id(okta_user_id)
    if not junction_user_id:
        raise HTTPException(status_code=404, detail="User not found")
    return [d.dict() for d in biomarker_data if d.junctionUserId == junction_user_id]

@app.get("/devices/{okta_user_id}")
async def get_device_status(okta_user_id: str):
    return devices

@app.get("/providers")
async def list_providers():
    return get_providers()

print("end of main.py")