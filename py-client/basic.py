import requests

#endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/"
result = requests.get(endpoint,json={"firstName":"Joseph"})
print(result.text)