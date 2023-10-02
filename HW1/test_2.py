from main import get, post, get_descr
import pytest
import yaml

with open('config.yaml') as f:
    conf = yaml.safe_load(f)

def test_step1(get_token):
    result = get(get_token)
    lst = result['data']
    lst_id =  [el["id"] for el in lst]
    assert 81155 in lst_id

def test_step2(get_token):
    result = post(get_token)
    assert result['description'] == conf['description']

def test_step3(get_token):
    list_of_dict = get_descr(get_token)['data']
    lst_descr =  [el["description"] for el in list_of_dict]
    assert conf['description'] in lst_descr

if __name__ == '__main__':
    pytest.main(['-v'])
