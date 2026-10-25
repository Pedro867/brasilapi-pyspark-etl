import requests

# Temporary example
response = requests.get('https://brasilapi.com.br/api/banks/v1')
print(response.json())