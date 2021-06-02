import requests

url = "https://api.extremecloudiq.com/ssids/users/{{user_id}}"

payload = ""
headers = {
  'accept': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
