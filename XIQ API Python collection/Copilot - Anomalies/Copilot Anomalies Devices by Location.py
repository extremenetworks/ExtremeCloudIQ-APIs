import requests

access_token = '***'

url = "https://api.extremecloudiq.com/copilot/anomalies/devices-by-location?anomalyType=POE_FLAPPING"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
