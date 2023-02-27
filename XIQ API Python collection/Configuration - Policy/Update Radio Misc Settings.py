import requests
import json

radio_misc_id = 0 # The radio miscellaneous settings ID
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/miscellaneous/{radio_misc_id}"

payload = json.dumps({
  "sla_throughput_level": "string",
  "radio_range": 10000
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
