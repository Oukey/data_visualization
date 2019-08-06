# hn_submissions.py

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

# Создание вызова API т сохранение ответа
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code:', r.status_code)

# Обработка информации о каждой статье
submission_ids = r.json()  # преобразование в список
submission_dicts, titles = [], []  # создание пустого списка для хранения словарей

for submission_id in submission_ids[:30]:  # цикл перебора 30 самых популярных статей
    # Создание отдельного вызова API для каждой статьи
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    # print(submission_r.status_code)  # вывод статуса запроса
    response_dict = submission_r.json()

    'СОздание словаря для текущей обрабатываемой статьи'
    submission_dict = {
        'title': response_dict['title'],  # сохранение заголовка статьи
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),  # сохранение ссылки
        'value': response_dict.get('descendants', 0)  # сохранение количества комментариев
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('value'), reverse=True)
# for submission_dict in submission_dicts:
#     print('\nTitle:', submission_dict['title'])
#     print('Discussion link:', submission_dict['link'])
#     print('Comments:', submission_dict['comments'])

for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])

# Построение визуализации
my_style = LS('333355', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_dont_size = 24
my_config.label_dont_size = 14
my_config.major_label_font_size = 18
my_config.width = 1200

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Top'
chart.x_labels = titles
chart.add('', submission_dicts)
chart.render_to_file('hn_submission.svg')
print('end')
