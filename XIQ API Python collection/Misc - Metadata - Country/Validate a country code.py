import requests

countryCode = 840
access_token = '***'

url = f"https://api.extremecloudiq.com/countries/{countryCode}/:validate"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
