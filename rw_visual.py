# rw_visual.py

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Построение случайного блуждания и нанесение точек на диаграмму
rw = RandomWalk()  # создает экземпляр класса случайного блуждания
rw.fill_walk()  # результат вычисления всех точек
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
