import requests

radio_qos_id = 0 # The radio QoS settings ID
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/wmm-qos/{radio_qos_id}"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
