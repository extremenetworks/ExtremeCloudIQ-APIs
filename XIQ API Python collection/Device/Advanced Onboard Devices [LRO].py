import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/devices/:advanced-onboard"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
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
}
# async: false (disabled)

response = requests.post(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
lro_url = response.headers.get('Location')
if lro_url:
    print(lro_url)
elif content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
