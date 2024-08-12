import requests

sn = 0 # serial number of the AP
access_token = '***'

url = f"https://api.extremecloudiq.com/ap/afc/interface/details/{sn}"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
