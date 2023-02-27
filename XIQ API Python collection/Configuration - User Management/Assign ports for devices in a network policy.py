import requests
import json

np_id = 0 # Network Policy ID
access_token = '***'

url = f"https://api.extremecloudiq.com/pcgs/key-based/network-policy-{np_id}/port-assignments"

payload = json.dumps({
  "port_assignments": [
    {
      "device_id": 0,
      "eth1_user_id": 0,
      "eth2_user_id": 0,
      "eth3_user_id": 0
    }
  ]
})
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
