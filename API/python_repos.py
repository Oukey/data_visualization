# python_repos.py

import requests

# Создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# Сохранение ответа API в переменной
response_dict = r.json()
print('Total repositories:', response_dict['total_count'])  # вывод общего количества репозиториев

# Анализ информации в репозиториях
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

# Анализ первого репозитория
repo_dict = repo_dicts[0]
print('\nSelected information about first repository:')
print('Name:', repo_dict['name'])  # имя проекта
print('Owner:', repo_dict['owner']['login'])  # Владелец
print('Stars:', repo_dict['stargazers_count'])  # Количество звезд
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])  # дата создания
print('Updated:', repo_dict['updated_at'])  # последнее обновление
print('Description:', repo_dict['description'])  # описание

# print('\nKeys:', len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)