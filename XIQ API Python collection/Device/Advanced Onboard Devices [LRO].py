import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/:advanced-onboard"

payload = json.dumps({
  "extreme": [
    {
      "serial_number": "string",
      "location": {
        "location_id": 0,
        "x": 0,
        "y": 0,
        "latitude": 0,
        "longitude": 0
      },
      "network_policy_id": 0,
      "hostname": "string"
    }
  ],
  "exos": [
    {
      "serial_number": "string",
      "location": {
        "location_id": 0,
        "x": 0,
        "y": 0,
        "latitude": 0,
        "longitude": 0
      },
      "network_policy_id": 0,
      "hostname": "string"
    }
  ],
  "voss": [
    {
      "serial_number": "string",
      "location": {
        "location_id": 0,
        "x": 0,
        "y": 0,
        "latitude": 0,
        "longitude": 0
      },
      "network_policy_id": 0,
      "hostname": "string"
    }
  ],
  "wing": [
    {
      "serial_number": "string",
      "mac_address": "string",
      "location": {
        "location_id": 0,
        "x": 0,
        "y": 0,
        "latitude": 0,
        "longitude": 0
      },
      "network_policy_id": 0,
      "hostname": "string"
    }
  ],
  "dell": [
    {
      "serial_number": "string",
      "service_tag": "string",
      "location": {
        "location_id": 0,
        "x": 0,
        "y": 0,
        "latitude": 0,
        "longitude": 0
      },
      "network_policy_id": 0,
      "hostname": "string"
    }
  ],
  "dt": [
    {
      "digital_twin_device": {
        "make": "SWITCH_ENGINE",
        "model": "DT_5320_16P_4XE",
        "os_type": "string",
        "os_version": "string",
        "vim_modules": [
          "DT_5520_VIM_4X"
        ],
        "feat_licenses": [
          "PRD_5000_PRMR"
        ]
      },
      "location": {
        "location_id": 0,
        "x": 0,
        "y": 0,
        "latitude": 0,
        "longitude": 0
      },
      "network_policy_id": 0,
      "hostname": "string"
    }
  ],
  "unmanaged": True
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
