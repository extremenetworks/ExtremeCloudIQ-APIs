import requests

audit_report_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/logs/audit/reports/{audit_report_id}"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
