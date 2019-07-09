# rw_visual.py

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной
while True:
    # Построение случайного блуждания и нанесение точек на диаграмму
    rw = RandomWalk()  # создает экземпляр класса случайного блуждания
    rw.fill_walk()  # результат вычисления всех точек
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input('Make another walk? (y/n):')
    if keep_running == 'n':
        break