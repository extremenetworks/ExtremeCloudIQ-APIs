import requests

url = "https://api.extremecloudiq.com/ccgs/{{ccg_id}}"

payload = ""
headers = {
  'accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
