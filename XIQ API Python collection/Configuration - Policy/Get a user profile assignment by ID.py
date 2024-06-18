import requests

user_profile_assignment_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/user-profile-assignments/{user_profile_assignment_id}"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
