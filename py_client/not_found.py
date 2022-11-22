import requests

endpoint = "http://localhost:8000/api/products/10000546460000000/"

get_response = requests.get(endpoint)
print(get_response.json())
