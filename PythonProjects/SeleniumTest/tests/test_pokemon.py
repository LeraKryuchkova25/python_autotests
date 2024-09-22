import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fd1e4192a014e84db37209f63fb5884a'
HEADER  = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 6325

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get_trainer_name = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response_get_trainer_name.json()["data"][0]["trainer_name"] == 'Лера'