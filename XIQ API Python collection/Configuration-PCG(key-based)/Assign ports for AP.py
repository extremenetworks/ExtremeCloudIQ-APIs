import requests

url = "https://api.extremecloudiq.com/pcg/key-based/ports/***"

payload="{\"pcg_port_assignment\":[{\"device_id\":***,\"eth1_user_id\":***,\"eth2_user_id\":***,\"eth3_user_id\":***}]}"
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': '***'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
