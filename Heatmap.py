import pandas as pd
import folium
from folium.plugins import HeatMap

# Загрузка данных из CSV файла
data = pd.read_csv('Chuy.csv')

# Создание нового столбца с годовыми осадками
data['Annual'] = data.iloc[:, 3:].sum(axis=1)

# Создание карты с фокусом на Чуйскую область
m = folium.Map(location=[42.8, 74.6], zoom_start=8)

# Нормализация данных для использования в цветовой шкале
min_precipitation = data['Annual'].min()
max_precipitation = data['Annual'].max()

# Преобразуем значения осадков в диапазон [0, 1] для градиента
data['Normalized'] = (data['Annual'] - min_precipitation) / (max_precipitation - min_precipitation)

# Подготовка данных для тепловой карты с использованием нормализованных значений
heat_data = [[row['Latitude'], row['Longitude'], row['Normalized']] for index, row in data.iterrows()]

# Добавление тепловой карты на карту с градиентом от красного к синему
gradient = {
    0: 'red',
    0.2: 'orange',
    0.4: 'yellow',
    0.6: 'lightgreen',
    0.8: 'cyan',
    1: 'blue'
}
HeatMap(heat_data, radius=25, gradient=gradient, blur=15).add_to(m)

# Добавление невидимых кругов с подсказками
for index, row in data.iterrows():
    tooltip_text = f"Точка #{index + 1}, Осадки: {row['Annual']} мм"
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=0,  # Нулевой радиус, чтобы круг был невидим
        color='transparent',  # Невидимый цвет
        fill_opacity=0,  # Полностью прозрачный
        tooltip=tooltip_text  # Добавляем подсказку
    ).add_to(m)

# Создание HTML легенды с вертикальной цветовой шкалой и числовыми значениями
legend_html = f'''
<div style="position: fixed; 
            top: 10px; right: 10px; width: 180px; height: 300px; 
            background-color: white; z-index:9999; font-size:14px;
            border:2px solid grey; padding: 10px; text-align: left;">
    <b>Precipitation (mm)</b><br>
    <div style="height: 250px; background: linear-gradient(to bottom, red, orange, yellow, lightgreen, cyan, blue); width: 30px; float: left; margin-right: 10px;"></div>
    <div style="position: relative; height: 250px; display: flex; flex-direction: column; justify-content: space-between;">
        <span style="text-align: right;">{round(min_precipitation, 1)}</span>
        <span style="text-align: right;">{round(max_precipitation, 1)}</span>
    </div>
</div>
'''

# Добавление HTML легенды на карту
m.get_root().html.add_child(folium.Element(legend_html))

# Сохранение карты в HTML
m.save('chuyskaya_oblast_heatmap_with_invisible_markers_and_tooltips.html')
