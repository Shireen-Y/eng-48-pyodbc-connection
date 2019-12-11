import requests

url = 'website'
response = requests.get(url)
print(response.status_code)