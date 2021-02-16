import requests

url = "https://api.extremecloudiq.com/hiq/context"

payload="{\n  \"reading_org_ids\": [\n   1\n  ],\n  \"creating_org_id\": 1\n}"
headers = {
  'Authorization': '***',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
