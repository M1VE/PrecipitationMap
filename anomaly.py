import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
data = pd.read_csv('chuy.csv')

# Определение аномальных значений
def detect_anomalies(df):
    anomalies = {}
    for month in df.columns[3:]:  # Пропускаем первые 3 столбца (Point, Longitude, Latitude)
        # Среднее и стандартное отклонение
        mean = df[month].mean()
        std_dev = df[month].std()
        threshold = mean + 2 * std_dev  # Определяем порог для аномалий
        # Фильтрация аномальных значений
        anomalies[month] = df[df[month] > threshold][['Point', month]]
    return anomalies

# Определение аномалий
anomalies = detect_anomalies(data)

# Вывод аномалий и частоты по месяцам
print("Anomalies:")
for month, anomaly_data in anomalies.items():
    print(f"\nMonth: {month}")
    print(anomaly_data)

# Анализ частоты аномалий
anomaly_counts = {month: len(anomaly_data) for month, anomaly_data in anomalies.items()}
frequency = pd.DataFrame(anomaly_counts.items(), columns=['Month', 'Anomaly Count'])
print("\nFrequency of anomalies per month:")
print(frequency)

# Визуализация частоты аномалий
plt.figure(figsize=(12, 6))
sns.barplot(x='Month', y='Anomaly Count', data=frequency)
plt.xticks(rotation=45)
plt.title('Frequency of Anomalies per Month')
plt.show()
