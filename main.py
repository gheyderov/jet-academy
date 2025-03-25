import requests

api_key = 'fcfb83a8'

movie_name = input()

response = requests.get(f'')


print(response.json())

print('helllo world')