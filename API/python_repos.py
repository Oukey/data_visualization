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
print('number of items:', len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],  # количество звезд
        'label': repo_dict['description'],  # описание проекта
    }
    plot_dicts.append(plot_dict)

# Построение визуализации
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_dont_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15  # сокращение длинных имен до 15 символов
my_config.show_y_guides = False  # скрытие горизонтальных линий на графике
my_config.width = 1000  # ширина диаграммы
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
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

# 370
