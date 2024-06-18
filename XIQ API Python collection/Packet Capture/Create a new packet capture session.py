import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/packetcaptures"

payload = json.dumps({
  "duration": 300,
  "capture_id_type": "DEVICE_IDS",
  "device_ids": [
    123000,
    123005
  ],
  "destination": "CLOUD",
  "filter": {
    "mac_addr": [
      "AABBCC001122"
    ],
    "ip_addr": [
      "192.168.11.255"
    ],
    "protocol": "USER_DEFINED",
    "protocol_number": 5,
    "port": 1024,
    "vlan": "2,3-5",
    "wlan": "some-ssid"
  },
  "capture_if": {
    "direction": "BOTH",
    "radio": "ALL",
    "wired_interface": "ETH0",
    "wireless_band": "2.4GHZ",
    "wired_filters": [
      "DHCP"
    ],
    "wireless_filters": [
      "DATA",
      "CONTROL"
    ]
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
