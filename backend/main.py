from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from vital.client import Vital
from vital.environment import VitalEnvironment
import os
from dotenv import load_dotenv

# SETUP
# Load env vars
load_dotenv()
api_key = os.getenv("JUNCTION_API_KEY")
if not api_key:
    raise RuntimeError("Missing JUNCTION_API_KEY in environment variables!")

# Initialize Vital API client
client = Vital(api_key=api_key, environment=VitalEnvironment.SANDBOX)

# Initialize FastAPI app
app = FastAPI(title="Happy Feet API", version="1.0.0")

# Enable CORS for frontend & backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # replace based on JC's port / setup
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Models -- handles & validates JSON data
class CreateUserRequest(BaseModel):
    client_user_id: str


# ROUTES
@app.post("/user")
def create_user(data: CreateUserRequest):
    """
    Creates a user in Junction
    """
    try:
        user = client.user.create(client_user_id=data.client_user_id)
        return user
    except Exception as e:
        message = str(e)
        if "Client user id already exists" in message and "user_id" in message:
            # Parse user_id from the message (temp fix)
            import re
            match = re.search(r"'user_id': '([^']+)'", message)
            if match:
                return {
                    "client_user_id": data.client_user_id,
                    "user_id": match.group(1),
                    "warning": "User already exists"
                }
        print("Error:", e)
        raise HTTPException(status_code=400, detail=message)

@app.get("/user/{user_id}")
def get_user(user_id: str):
    """
    Get a Junction user by user_id
    """
    try:
        user = client.user.get(user_id=user_id)
        return user
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=404, detail=str(e))


@app.post("/link-token")
def generate_link_token(data: CreateUserRequest):
    """
    Generates a link token to launch wearable widget 
    """
    try:
        # Fetch the Vital user_id first
        user = client.user.create(client_user_id=data.client_user_id)
        user_id = user["user_id"]
        token = client.link.token(user_id=user_id)
        return token
    except Exception as e:
        message = str(e)
        # Extract user_id from error if user already exists
        import re
        match = re.search(r"'user_id': '([^']+)'", message)
        if match:
            user_id = match.group(1)
            token = client.link.token(user_id=user_id)
            return token
        print("Error:", e)
        raise HTTPException(status_code=500, detail=message)

@app.get("/providers")
def list_providers():
    """
    Returns a list of available wearable providers
    """
    try:
        providers = client.providers.get_all()
        return providers
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/connections/{user_id}")
def get_user_connections(user_id: str):
    """
    Returns wearables and their connection status by user_id
    """
    try:
        connections = client.connections.get_user_connections(user_id=user_id)
        return connections
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/webhook")
async def receive_webhook(request: Request):
    """
    Handle webhook events sent by Junction (ex. new step data)
    """
    try:
        payload = await request.json()
        # TODO: store or process data as needed
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid webhook payload")
    
@app.get("/activity/{user_id}")
def get_activity(user_id: str):
    """
    Get step/activity data by user_id
    """
    try:
        data = client.activity.get_user_activity(user_id=user_id)
        return data
    except Exception as e:
        print("Error getting activity:", e)
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/sleep/{user_id}")
def get_sleep(user_id: str):
    """
    Get sleep data by user_id
    """
    try:
        data = client.sleep.get_user_sleep(user_id=user_id)
        return data
    except Exception as e:
        print("Error getting sleep:", e)
        raise HTTPException(status_code=500, detail=str(e))
