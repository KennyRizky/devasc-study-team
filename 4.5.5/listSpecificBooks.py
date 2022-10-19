import json
import requests

id = int(input("Masukkan Id buku Anda: "))
title = input("Masukkan title buku Anda: ")
author = input("Masukkan author buku Anda: ")

url = "http://library.demo.local/api/v1/books"

params = {"id": id,
            "title": title,
            "author": author
            }

headers = {
    "Content-Type": "application/json",
    "x-api-key": "cisco|qYYUInVquBFm4q7tDK3jvqk7HxLfqgWb2Na0S1Zk_Lk"
}

sendK = requests.get(url, headers = headers, data = json.dumps(params))
print(sendK.text)