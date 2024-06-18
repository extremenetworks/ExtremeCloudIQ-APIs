import requests

report_name = 'string'
access_token = '***'

url = f"https://api.extremecloudiq.com/account/viq/download?reportName={report_name}"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
