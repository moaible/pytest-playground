import requests

def mod():
    response = requests.get("https://httpbin.org/get")
    return response
