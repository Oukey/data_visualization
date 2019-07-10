# rw_visual.py

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной
while True:
    # Построение случайного блуждания и нанесение точек на диаграмму
    rw = RandomWalk(50000)  # создает экземпляр класса случайного блуждания
    rw.fill_walk()  # результат вычисления всех точек

    # Вывод точек и отображение диаграммы
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # Выделение первой и последней точек
    # Начаьная точка - зеленая, последняя - красная
    # edgecolors='none' - убирает черный контур каждой точки
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Удаление осей
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n):')
    if keep_running == 'n':
        break

# 326