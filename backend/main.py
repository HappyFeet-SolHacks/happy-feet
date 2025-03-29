from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from vital.client import Vital
from vital.environment import VitalEnvironment
import os
from dotenv import load_dotenv

# Load env vars
load_dotenv()
api_key = os.getenv("VITAL_API_KEY")

client = Vital(api_key=api_key, environment=VitalEnvironment.SANDBOX)

app = FastAPI()

class CreateUserRequest(BaseModel):
    client_user_id: str

@app.post("/user")
def create_user(data: CreateUserRequest):
    try:
        user = client.user.create(client_user_id=data.client_user_id)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/user/{user_id}")
def get_user(user_id: str):
    try:
        user = client.user.get(user_id=user_id)
        return user
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/providers")
def get_providers():
    try:
        providers = client.providers.get_all()
        return providers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/connections/{user_id}")
def get_connections(user_id: str):
    try:
        connections = client.connections.get_user_connections(user_id=user_id)
        return connections
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
