import requests

anomaly_id = 0
device_id = 0
lastDetectedTime = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/copilot/anomalies/poeflapping/lldp-cdp-info?anomalyId={str(anomaly_id)}&deviceId={str(device_id)}&lastDetectedTime={str(lastDetectedTime)}"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
