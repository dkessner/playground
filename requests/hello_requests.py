#!/usr/bin/env python
#
# hello_requests.py
#


import requests


search_url = "https://api.thecatapi.com/v1/images/search"


result = requests.get(search_url)

url = result.json()[0]['url']

print(url)

image = requests.get(url)
with open("image.jpg", "wb") as f:
    f.write(image.content)




