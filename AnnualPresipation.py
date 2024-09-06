import pandas as pd
import matplotlib.pyplot as plt
# Построение годового графика осадков для каждой точки
# Загрузка данных из файла
data = pd.read_csv('Chuy.csv')

# Добавление столбца с годовой суммой осадков
data['Annual'] = data.iloc[:, 3:].sum(axis=1)

# Построение графика
plt.figure(figsize=(10, 6))
plt.bar(data['Point'], data['Annual'], color='skyblue')
plt.xlabel('Point')
plt.ylabel('Annual Precipitation (mm)')
plt.title('Annual Precipitation for Each Point')
plt.show()
