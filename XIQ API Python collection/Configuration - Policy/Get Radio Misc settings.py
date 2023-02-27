import requests

radio_misc_id = 0 # The radio miscellaneous settings ID
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/miscellaneous/{radio_misc_id}"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
