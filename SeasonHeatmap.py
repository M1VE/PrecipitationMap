import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных из файла
data = pd.read_csv('Chuy.csv')

# Рассчитываем средние значения осадков для каждого сезона
data['Winter'] = data[['Dec', 'Jan', 'Feb']].mean(axis=1)
data['Spring'] = data[['Mar', 'Apr', 'May']].mean(axis=1)
data['Summer'] = data[['Jun', 'Jul', 'Aug']].mean(axis=1)
data['Autumn'] = data[['Sep', 'Oct', 'Nov']].mean(axis=1)

# Подготовка данных для тепловой карты
seasonal_data = data[['Point', 'Longitude', 'Latitude', 'Winter', 'Spring', 'Summer', 'Autumn']]

# Настройка графиков
fig, axes = plt.subplots(2, 2, figsize=(18, 14))
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
colors = ['coolwarm_r', 'coolwarm_r', 'coolwarm_r', 'coolwarm_r']

for i, season in enumerate(seasons):
    ax = axes[i//2, i%2]
    # Создание тепловой карты
    sns.heatmap(data.pivot_table(values=season, index='Latitude', columns='Longitude'),
                cmap=colors[i], ax=ax, cbar_kws={'label': 'Precipitation (mm)'},
                annot=True, fmt='.1f', annot_kws={"size": 8})
    ax.set_title(f'{season} Precipitation', fontsize=16)
    ax.set_xlabel('Longitude', fontsize=14)
    ax.set_ylabel('Latitude', fontsize=14)
    ax.tick_params(axis='both', which='major', labelsize=12)
    # Поворот меток осей для избежания наложения
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

# Настройка отступов
plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.show()
