
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://jiragod.atlassian.net/rest/api/3/project"

API_TOKEN=""

auth = HTTPBasicAuth("danielhuebner1998@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)

print(output)