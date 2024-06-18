import requests

alert_report_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/alerts/reports/{str(alert_report_id)}"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
