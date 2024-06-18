import requests

countryAlpha2Code = 'US'
access_token = '***'

url = f"https://api.extremecloudiq.com/countries/{countryAlpha2Code}/states"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
