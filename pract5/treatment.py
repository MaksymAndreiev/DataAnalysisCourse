import pandas as pd
from scipy.stats import ttest_rel

# Завантаження даних з файлу
df = pd.read_excel('treatment.xlsx')

# Виконання t-критерію для залежних вибірок
t_statistic, p_value = ttest_rel(df['Pressure_before'], df['Pressure_after'])

# Виведення результатів
print('t-статистика:', t_statistic)
print('p-значення:', p_value)
