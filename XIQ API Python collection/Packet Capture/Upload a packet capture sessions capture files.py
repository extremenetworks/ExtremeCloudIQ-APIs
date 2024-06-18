import requests

pcap_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/packetcaptures/{pcap_id}/:upload"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
