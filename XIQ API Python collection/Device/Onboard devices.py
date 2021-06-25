import requests

url = "https://api.extremecloudiq.com/devices/"

payload="{\n  \"extreme\": {\n    \"sns\": [\n      \"string\"\n    ]\n  },\n  \"exos\": {\n    \"sns\": [\n      \"string\"\n    ]\n  },\n  \"voss\": {\n    \"sns\": [\n      \"string\"\n    ]\n  },\n  \"wing\": {\n    \"sn_to_mac\": {\n      \"additionalProp1\": \"string\",\n      \"additionalProp2\": \"string\",\n      \"additionalProp3\": \"string\"\n    }\n  },\n  \"dell\": {\n    \"sn_to_st\": {\n      \"additionalProp1\": \"string\",\n      \"additionalProp2\": \"string\",\n      \"additionalProp3\": \"string\"\n    }\n  }\n}"
headers = {
  'Authorization': '***',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
