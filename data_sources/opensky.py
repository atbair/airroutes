import requests

CLIENT_ID = "atbairlines-api-client"
CLIENT_SECRET = "P8lyoCtpJ3psozKY0HZ1IpbtrYOUIFPq"

# Step 1: get token
auth_url = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"

auth_response = requests.post(
    auth_url,
    data={
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
)

token = auth_response.json()["access_token"]
print(token)
# Step 2: use token
headers = {
    "Authorization": f"Bearer {token}"
}

data = requests.get(
    "https://opensky-network.org/api/states/all",
    headers=headers
).json()

print(len(data["states"]))