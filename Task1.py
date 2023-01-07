import requests
response = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")

new = response.json()
new_dict = {}
for i in new:
    y = i['name']
    if y == 'Hulk' or y == 'Thanos' or y == 'Captain America':
        x = i['powerstats']['intelligence']
        new_dict[y] = x

print(max(new_dict.items()))
