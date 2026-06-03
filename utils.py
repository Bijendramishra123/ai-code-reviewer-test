import requests

# Hardcoded API endpoint
API_URL = "http://internal-api.local/secret"

def fetch_data(user_id):
    response = requests.get(f"{API_URL}/users/{user_id}")
    return response.json()
