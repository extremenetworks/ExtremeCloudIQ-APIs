import requests

url = "https://api.extremecloudiq.com/pcg/key-based/***/"

payload="{\"enabled\":true,\"ssid_name\":\"string\",\"user_ids\":[0]}"
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': '***'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
