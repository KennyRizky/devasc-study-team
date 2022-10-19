from email import header
from email.mime import application
import json
from wsgiref import headers
import requests

username = input("Masukkan username Anda: ")
password = input("Masukkan password Anda: ")

url = "http://library.demo.local/api/v1/loginViaJSON"

params = {"username": username,
            "password": password
            }

headers = {
    "Content-Type": "application/json"
}

sendK = requests.post(url, headers = headers, data = json.dumps(params))
print(sendK.text)

