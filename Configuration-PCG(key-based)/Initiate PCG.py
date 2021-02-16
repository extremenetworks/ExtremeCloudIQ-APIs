import requests

url = "https://api.extremecloudiq.com/pcg/key-based"

payload="{\"policy_name\":\"***\",\"ssid_name\":\"***\",\"users\":[{\"name\":\"***\",\"email\":\"***\",\"user_group_name\":\"***\"}]}"
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': ''
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
