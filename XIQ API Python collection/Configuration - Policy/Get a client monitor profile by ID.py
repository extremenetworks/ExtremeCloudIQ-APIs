import requests

cient_mon_profile_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/client-monitor-profiles/{cient_mon_profile_id}"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
