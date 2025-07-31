import requests
         
baseUrl = 'https://api.extremecloudiq.com'
hotspot_id = 'Hotspot profile ID'
access_token = '***'

url = f"{baseUrl}/hotspot-profiles/{hotspot_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "hessid": "ba:aE:EC:84:81:70",
  "domain_name": "string",
  "operator_names": [
    {
      "name": "string",
      "language": "qff"
    }
  ],
  "venue": {
    "venue_group": "UNSPECIFIED",
    "venue_type": "UNSPECIFIED",
    "names": [
      {
        "name": "string",
        "language": "zju"
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
      "consortium_id": "d22896b1d4a46137cF2BDE9f9",
      "description": "string"
    }
  ],
  "cellular_networks": [
    {
      "mcc": "246",
      "mnc": "60",
      "description": "string"
    }
  ],
  "service_provider_ids": [
    0
  ]
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
