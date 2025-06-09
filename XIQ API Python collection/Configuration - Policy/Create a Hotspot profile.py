import requests
         
baseUrl = 'api.extremecloudiq.com'
access_token = '***'

url = f"https://{baseUrl}/hotspot-profiles"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "hessid": "71:4A:5C:6C:Fa:e1",
  "domain_name": "string",
  "operator_names": [
    {
      "name": "string",
      "language": "mnt"
    }
  ],
  "venue": {
    "venue_group": "UNSPECIFIED",
    "venue_type": "UNSPECIFIED",
    "names": [
      {
        "name": "string",
        "language": "nrc"
      }
    ]
  },
  "access_network_type": "PRIVATE",
  "dgaf": True,
  "ipv4_availability": "NOT_AVAILABLE",
  "ipv6_availability": "NOT_AVAILABLE",
  "wan_metrics": {
    "status": "DOWN",
    "downlink_speed": 4194304,
    "uplink_speed": 4194304
  },
  "connection_capabilities": [
    {
      "protocol": "ESP",
      "port_number": 65535,
      "status": "CLOSED"
    }
  ],
  "qos_map": {
    "dscp_ranges": [
      {
        "ah_class": 7,
        "dscp_range_start": 63,
        "dscp_range_end": 63
      }
    ],
    "dscp_exceptions": [
      {
        "ah_class": 7,
        "dscp_value": 63
      }
    ]
  },
  "gas_comeback_delay": 65535,
  "anqp_domain_id": 65535,
  "online_signup": {
    "network_auth_type": "ACCEPTANCE_TERMS",
    "redirection_url": "string",
    "ssid_id": 0
  },
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
      "consortium_id": "886eaD",
      "description": "string"
    }
  ],
  "cellular_networks": [
    {
      "mcc": "424",
      "mnc": "98",
      "description": "string"
    }
  ],
  "service_provider_ids": [
    0
  ]
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
