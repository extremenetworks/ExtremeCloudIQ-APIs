import requests

ccg_id = 0 # Cloud Config Group ID
access_token = '***'

url = f"https://api.extremecloudiq.com/ccgs/{ccg_id}"

payload = ""
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
