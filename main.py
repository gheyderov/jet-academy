import requests

api_key = 'fcfj34j'

movie_name = input()



response = requests.get(f'')


print(response.json())

print('helllo world')