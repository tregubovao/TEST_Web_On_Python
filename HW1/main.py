# Написать тест с использованием pytest и requests, в котором:
# Адрес сайта, имя пользователя и пароль хранятся в config.yaml
# conftest.py содержит фикстуру авторизации по адресу 
# https://test-stand.gb.ru/gateway/login с передачей параметров “username" и "password" 
# и возвращающей токен авторизации
# Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого пользователя, 
# для этого выполняется get запрос по адресу https://test-stand.gb.ru/api/posts c хедером, 
# содержащим токен авторизации в параметре "X-Auth-Token". 
# Для отображения постов другого пользователя передается "owner": "notMe".

# Задание: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, а потом проверяется его наличие на сервере по полю «описание».

import yaml
import requests


with open('config.yaml') as f:
    conf = yaml.safe_load(f)

def get_token():
    responce = requests.post(url=conf['url'], data={'username': conf['username'], 'password': conf['passwd']})
    return responce.json()['token'] 

def get(token: str):
    resource = requests.get(conf["url_post"], headers={"X-Auth-Token": token}, params={"owner": "notMe"})
    return resource.json()

def post(token: str):
    resource = requests.post(conf["url_post"], headers={"X-Auth-Token": token}, 
                             params={"title": conf['title'], "description": conf['description'], 
                                     "content": conf['content']})
    return resource.json()

def get_descr(token: str):
    resource = requests.get(conf["url_post"], headers={"X-Auth-Token": token}, 
                            params={"description": conf['description']})
    return resource.json()



if __name__ == '__main__':
    temp = get_token()
    print(get_descr(temp)['data'])
    



