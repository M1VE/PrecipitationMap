import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
data = pd.read_csv('Chuy.csv')

# Переменные для месяцев
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Уникальные цвета для каждого месяца
colors = [
    'b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'gray'
]

# Создание графика
plt.figure(figsize=(14, 8))
for i, month in enumerate(months):
    plt.plot(data.index, data[month], label=month, color=colors[i], marker='o')

plt.title('Распределение осадков по месяцам')
plt.xlabel('Точка данных')
plt.ylabel('Осадки (мм)')
plt.legend(title='Месяц')
plt.grid(True)
plt.tight_layout()
plt.show()
