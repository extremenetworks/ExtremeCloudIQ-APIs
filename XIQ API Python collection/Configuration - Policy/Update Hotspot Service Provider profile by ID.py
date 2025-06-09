import requests
         
baseUrl = 'api.extremecloudiq.com'
hotspot_service_provider_id = 'Hotspot Service Provider profile ID'
access_token = '***'

url = f"https://{baseUrl}/hotspot-service-provider-profiles/{hotspot_service_provider_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "description": "string",
  "friendly_names": [
    {
      "name": "string",
      "language": "ngf"
    }
  ],
  "descriptions": [
    {
      "name": "string",
      "language": "pxy"
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
      "consortium_id": "Dab7c2C5a569C2a4A6",
      "description": "string"
    }
  ],
  "cellular_networks": [
    {
      "mcc": "055",
      "mnc": "19",
      "description": "string"
    }
  ],
  "osu_uri": "string",
  "osu_methods": [
    "OMA_DM"
  ],
  "osu_nai": "string"
}


response = requests.put(url, headers=headers, params=params)

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
