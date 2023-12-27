
import requests

# Define the data payload
data = {
    "code": "EyU0vN90bzAAAAAAAAAA9DiN73k7z2S_fbGy3NTbnFo",
    "grant_type": "authorization_code",
    "client_id": "sl0etqo83otxrsk",
    "client_secret": "jmd9gizqc9lk4qa",
    "redirect_uri": "http://127.0.0.1:8000/"
}

# Send the POST request
response = requests.post("https://api.dropbox.com/oauth2/token", data=data)

# Parse the response
token_data = response.json()

# Extract the access token
access_token = token_data['access_token']

print("Status code:", response.status_code)
print("Response:", response.json())
