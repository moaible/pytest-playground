import requests

def mod() -> requests.Response:
    response = requests.get("https://httpbin.org/get")
    return response
