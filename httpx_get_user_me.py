import httpx

login_payload = {
  "email": "testing_api@example.com",
  "password": "qwerty123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_data = login_response.json()
access_token = login_response_data['token']['accessToken']
client = httpx.Client(headers={"authorization": f"Bearer {access_token}"})

me_response = client.get("http://localhost:8000/api/v1/users/me")

print(me_response.status_code)
print(me_response.json())
print(me_response.request.headers)
