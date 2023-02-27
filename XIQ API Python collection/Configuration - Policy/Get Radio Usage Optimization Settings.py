import requests

radio_usage_opt_id = 0 # The radio usage optimization settings ID
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/radio-usage-opt/{radio_usage_opt_id}"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
