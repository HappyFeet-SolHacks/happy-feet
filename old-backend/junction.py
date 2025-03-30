from vital.client import Vital
from vital.environment import VitalEnvironment
from vital.types.o_auth_providers import OAuthProviders
import os
from dotenv import load_dotenv

load_dotenv()

client = Vital(
    api_key=os.getenv("JUNCTION_API_KEY"),
    environment=VitalEnvironment.SANDBOX,
)

def create_user(user_id: str):
    return client.user.create(client_user_id=user_id)

def generate_link_token(user_id: str, provider: str = OAuthProviders.OURA):
    return client.link.create(user_id=user_id, provider=provider)

def get_providers():
    return client.providers.get_all()


'''
const wearableProviders = [
  { name: 'fitbit', available: true },
  { name: 'Apple Watch', available: false },
];

const summaryData = [
  { category: 'sleep (hrs)', value: 8 },
  { category: 'activity (steps)', value: 7000 },
];
'''