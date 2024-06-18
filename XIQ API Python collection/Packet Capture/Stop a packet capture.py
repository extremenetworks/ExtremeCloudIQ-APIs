import requests
import json

pcap_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/packetcaptures/{pcap_id}/:stop"

payload = json.dumps({
  "device_ids": [
    0
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
