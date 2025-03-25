import requests

api_key = 'fcfb83a8'

movie_name = input()

response = requests.get(f'https://www.omdbapi.com/?t={movie_name}&apikey={api_key}')

print(response.json())