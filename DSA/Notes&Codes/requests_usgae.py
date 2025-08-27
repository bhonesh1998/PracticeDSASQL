
# API

# json response

import sys
import requests
import json

url = "https://itunes.apple.com/search?=entity=song&limit=1&term=weezer"

response = requests.get(url)

print(response.json())

print(json.dumps(response.json(),indent=2))





