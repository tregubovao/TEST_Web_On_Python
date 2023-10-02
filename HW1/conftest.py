import pytest
import yaml
import requests

with open('config.yaml') as f:
    conf = yaml.safe_load(f)

@pytest.fixture()
def get_token():
    responce = requests.post(url=conf['url'], data={'username': conf['username'], 'password': conf['passwd']})
    return responce.json()['token'] 
