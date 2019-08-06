# hn_submissions.py

import requests

from operator import itemgetter

# Создание вызова API т сохранение ответа
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code:', r.status_code)

# Обработка информации о каждой статье
submission_ids = r.json()  # преобразование в список
submission_dicts = []  # создание пустого списка для хранения словарей
for submission_id in submission_ids[:30]:  # цикл перебора 30 самых популярных статей
    # Создание отдельного вызова API для каждой статьи
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)  # вывод статуса запроса
    response_dict = submission_r.json()

    'СОздание словаря для текущей обрабатываемой статьи'
    submission_dict = {
        'title': response_dict['title'],  # сохранение заголовка статьи
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),  # сохранение ссылки
        'comments': response_dict.get('descendants', 0)  # сохранение количества комментариев
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
for submission_dict in submission_dicts:
    print('\nTitle:', submission_dict['title'])
    print('Discussion link:', submission_dict['link'])
    print('Comments:', submission_dict['comments'])
