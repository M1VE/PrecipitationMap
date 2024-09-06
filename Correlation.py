import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
data = pd.read_csv('Chuy.csv')

# Удаление столбцов, не содержащих данные об осадках
monthly_precipitation = data.drop(columns=['Point', 'Longitude', 'Latitude'])

# Расчет корреляционной матрицы
correlation_matrix = monthly_precipitation.corr()

# Построение тепловой карты корреляционной матрицы
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1, cbar=True)
plt.title('Корреляционная матрица осадков по месяцам')
plt.show()
