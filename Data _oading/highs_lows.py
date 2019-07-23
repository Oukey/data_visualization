# highs_Lows.py

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# чтение дат и температурных максимумов и минимумов из файла
filename = 'sitka_weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)

        # for index, column_header in enumerate(header_row):
        #     print(index, column_header)
        '''
        0 STATION
        1 NAME
        2 DATE
        3 PRCP
        4 TAVG
        5 TMAX
        6 TMIN
        '''

# Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Форматирование диграммы
plt.title("Daily high and lows temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
