import requests
import json

url = "https://api.extremecloudiq.com/ccgs/{{ccg_id}}"

payload = "{\n  \"name\": \"\",\n  \"description\": \"Update CCG device list\",\n  \"device_ids\": [\n    {{id}}\n    \n  ]\n}"
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
