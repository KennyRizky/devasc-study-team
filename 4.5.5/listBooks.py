import json
import requests

url = "http://library.demo.local/api/v1/books"

headers = {
    "accept": "application/json"
}

sendK = requests.get(url, headers = headers)
print(sendK.text)