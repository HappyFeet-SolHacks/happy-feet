# models.py
from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    client_user_id: str

class DeviceConnection(BaseModel):
    junctionUserId: str
    provider: str
    status: str  # "connected" | "unavailable" | "coming soon"
    lastSync: datetime

class BiomarkerReading(BaseModel):
    junctionUserId: str
    type: str  # "sleep" | "activity" | "heartRate"
    timestamp: datetime
    minRange: int
    maxRange: int