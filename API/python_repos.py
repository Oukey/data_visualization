# python_repos.py

import requests
import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

# Создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Сохранение ответа API в переменной
response_dict = r.json()
print('Total repositories:', response_dict['total_count'])  # вывод общего количества репозиториев

# Анализ информации о репозиториях
repo_dicts = response_dict['items']
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    description = repo_dict['description']
    if not description:
        description = 'No description provided'
    plot_dict = {
        'value': repo_dict['stargazers_count'],  # количество звезд
        'label': description,  # описание проекта
        'xlink': repo_dict['html_url'],
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

# 373  БАГ!!! 'decode'
