import requests

endpoint = "https://httpbin.org/anything"
result = requests.get(endpoint,json={"firstName":"Joseph"})
print(result.json())