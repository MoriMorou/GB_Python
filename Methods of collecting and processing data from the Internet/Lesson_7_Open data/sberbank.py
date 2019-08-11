import matplotlib.pyplot as plt
import csv

with open('opendata.csv', 'r') as f:
    reader = csv.DictReader(f)
    field_names = reader.fieldnames
    print(field_names)
    money = []
    date = []
    for row in reader:
        #print(row)
        if row['name'] == 'Средняя зарплата' and row['region'] == 'Томская область':
            date.append(row['date'])
            money.append(int(row['value']))

plt.plot(date, money)
plt.show()
