import requests
import json
import base64
import os

url = "https://dev61008.service-now.com/api/now/table/incident"
username = os.environ["SERVICENOW_USERNAME"]
password = os.environ["SERVICENOW_PASSWORD"]
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vYzg2ZjljMDAtNTY5Yi0xMWVjLThjNmUtYjE2MmM5MjUxYmVl"

payload = {
    "description": "Problemas al cargar sitio web",
    "short_description": "Incidente solicitado desde Python",
    "category": "Network",
    "caller_id": "abraham.lincoln@example.com"
}

data = json.dumps(payload)

headers = {
  "Content-Type": "application/json"
}

response = requests.post(url, auth=(username, password), headers=headers, data=data)

print(response.text)