import requests

radio_profile_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/{radio_profile_id}"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
