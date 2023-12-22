import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf

attitude = pd.read_excel("attitude.xlsx")

# перегляд перших 5 рядків даних
print(attitude.head())

# перевіряємо наявність пропущених даних
print("Пропущені данні:")
print(attitude.isnull().sum())

# статистика описових характеристик
print(attitude.describe())

# встановлюємо цільову змінну та факторні змінні
target_var = 'rating'
predictor_vars = ['complaints', 'privileges', 'learning', 'raises', 'critical', 'advance']

# побудова моделей парної лінійної регресії для кожної факторної змінної
for predictor in predictor_vars:
    model = smf.ols(f"{target_var} ~ {predictor}", data=attitude).fit()
    print(f"Linear Regression Model for {target_var} ~ {predictor}:")
    print(model.summary())

# Побудова моделей множинної регресії для різних комбінацій факторних змінних
model1 = smf.ols("rating ~ complaints + privileges + learning + raises + critical + advance", data=attitude).fit()
model2 = smf.ols("rating ~ complaints + privileges + learning + raises + advance", data=attitude).fit()
model3 = smf.ols("rating ~ complaints + privileges + learning + critical + advance", data=attitude).fit()
model4 = smf.ols("rating ~ complaints + learning + raises + critical + advance", data=attitude).fit()

print(f"Multiple Regression Model for {target_var} ~ complaints + privileges + learning + raises + critical + advance:")
print(model1.summary())
print(f"Multiple Regression Model for {target_var} ~ complaints + privileges + learning + raises + advance:")
print(model2.summary())
print(f"Multiple Regression Model for {target_var} ~ complaints + privileges + learning + critical + advance:")
print(model3.summary())
print(f"Multiple Regression Model for {target_var} ~ complaints + learning + raises + critical + advance:")
print(model4.summary())
