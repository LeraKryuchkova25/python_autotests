import requests
URL = 'https://api.pokemonbattle.ru/v2'

TOKEN = 'fd1e4192a014e84db37209f63fb5884a'
HEADER  = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "73158",
    "name": "Daemon",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "73158"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)
