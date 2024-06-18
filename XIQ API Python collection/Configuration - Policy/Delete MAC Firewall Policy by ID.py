import requests

mac_firewall_policy_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/mac-firewall-policy/{mac_firewall_policy_id}"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
