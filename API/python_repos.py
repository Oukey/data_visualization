# python_repos.py

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# Сохранение ответа API в переменной
response_dict = r.json()
print('Total repositories:', response_dict['total_count'])  # вывод общего количества репозиториев

# Анализ информации о репозиториях
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Построение визуализации
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')


# print('\nName:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Description:', repo_dict['description'])

# # Анализ первого репозитория
# repo_dict = repo_dicts[0]
# print('\nSelected information about first repository:')
# print('Name:', repo_dict['name'])  # имя проекта
# print('Owner:', repo_dict['owner']['login'])  # Владелец
# print('Stars:', repo_dict['stargazers_count'])  # Количество звезд
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])  # дата создания
# print('Updated:', repo_dict['updated_at'])  # последнее обновление
# print('Description:', repo_dict['description'])  # описание

# print('\nKeys:', len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
