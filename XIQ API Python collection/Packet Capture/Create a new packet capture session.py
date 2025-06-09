import requests
         
baseUrl = 'api.extremecloudiq.com'
access_token = '***'

url = f"https://{baseUrl}/packetcaptures"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "duration" : 300,
  "capture_id_type" : "DEVICE_IDS",
  "device_ids" : [ 123000, 123005 ],
  "destination" : "CLOUD",
  "filter" : {
    "mac_addr" : [ "AABBCC001122" ],
    "ip_addr" : [ "192.168.11.255" ],
    "protocol" : "USER_DEFINED",
    "protocol_number" : 5,
    "port" : 1024,
    "vlan" : "2,3-5",
    "wlan" : "some-ssid"
  },
  "capture_if" : {
    "direction" : "BOTH",
    "radio" : "ALL",
    "wired_interface" : "ETH0",
    "wireless_band" : "2.4GHZ",
    "wired_filters" : [ "DHCP" ],
    "wireless_filters" : [ "DATA", "CONTROL" ]
  }
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
