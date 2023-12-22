import pandas as pd
from scipy.stats import chi2_contingency

# завантажити дані з csv-файлу
data = pd.read_csv("Максим Андреєв - grants.csv", encoding='cp1251', sep=";")

# побудувати контингенційну таблицю
cont_table1 = pd.crosstab(data.field, data.status)
cont_table2 = pd.crosstab(data.years_in_uni, data.status)

# виконати хі-квадрат тест
chi2_1, p1, _, _ = chi2_contingency(cont_table1)
chi2_2, p2, _, _ = chi2_contingency(cont_table2)

# вивести результати тесту
print("Хі-квадрат статистика (галузь):", chi2_1)
print("p1-значення (галузь):", p1)
print("Хі-квадрат статистика (роки в університеті):", chi2_2)
print("p1-значення (роки в університеті):", p2)

