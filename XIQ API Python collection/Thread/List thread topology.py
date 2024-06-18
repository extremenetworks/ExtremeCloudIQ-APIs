import requests

networkConfigIds = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/thread/topology?networkConfigIds={networkConfigIds}"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
