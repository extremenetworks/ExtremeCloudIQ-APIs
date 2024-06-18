import requests

network_service_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/network-services/{network_service_id}"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
