import requests

api_key = 'fcfb83a8'

movie_name = input()

response = requests.get('test')

print(response.json())