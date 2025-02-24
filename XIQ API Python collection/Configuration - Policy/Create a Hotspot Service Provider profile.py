import requests
         

access_token = '***'

url = f"https://api.extremecloudiq.com/hotspot-service-provider-profiles"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "description": "string",
  "friendly_names": [
    {
      "name": "string",
      "language": "qcc"
    }
  ],
  "descriptions": [
    {
      "name": "string",
      "language": "svp"
    }
  ],
  "icon_files": [
    {
      "file_directory_name": "string",
      "file": "string",
      "language": "string"
    }
  ],
  "nai_realms": [
    {
      "name": "string",
      "description": "string",
      "eap_methods": [
        "EAP_TTLS_PAP"
      ],
      "encoding_type": "RFC_4282"
    }
  ],
  "roaming_consortiums": [
    {
      "consortium_id": "9b0E76e2717024",
      "description": "string"
    }
  ],
  "cellular_networks": [
    {
      "mcc": "408",
      "mnc": "85",
      "description": "string"
    }
  ],
  "osu_uri": "string",
  "osu_methods": [
    "OMA_DM"
  ],
  "osu_nai": "string"
}


response = requests.post(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
if content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
