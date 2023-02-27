import requests

access_token = '***'

viq_id = 0 # The account ID to switch, switch back to home ExtremeCloud IQ account if not provide

url = f"https://api.extremecloudiq.com/account/:switch?id={viq_id}"

payload = ""
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
