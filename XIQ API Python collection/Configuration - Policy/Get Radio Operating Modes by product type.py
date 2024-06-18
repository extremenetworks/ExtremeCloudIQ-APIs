import requests

productType = ''
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-operating-mode?productType={productType}"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
