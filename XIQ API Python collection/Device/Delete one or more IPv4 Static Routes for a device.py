import requests

device_id = 0
ipv4StaticRouteId = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/config/vlan-ipv4-static?staticRouteIds={ipv4StaticRouteId}"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
