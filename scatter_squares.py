# scatter_squares.py

import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# plt.scatter(x_values, y_values, s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='None', s=40)

# Назначение заголовка диаграмм и меток осей
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Назначение размера шрифта делений на осях
plt.tick_params(axis='both', which='major', labelsize=14)
# Назначение диапазона для каждой оси
plt.axis([0, 1100, 0, 1100000])

plt.show()

