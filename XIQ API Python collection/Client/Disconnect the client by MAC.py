import requests

client_mac = '4AE654B84399'
access_token = '***'

url = f"https://api.extremecloudiq.com/clients/byMac/{client_mac}"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
