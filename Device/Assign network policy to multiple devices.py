import requests

url = "https://api.extremecloudiq.com/devices/network-policy/"

payload="{\"devices\":{\"ids\":[***]},\"network_policy_id\":***}"
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': '***'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
