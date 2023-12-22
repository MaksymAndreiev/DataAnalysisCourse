import warnings

import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

warnings.filterwarnings("ignore",
                        message="Support for FigureCanvases without a required_interactive_framework attribute was deprecated in Matplotlib 3.6")

attitude = pd.read_excel("attitude.xlsx")

# перегляд перших 5 рядків даних
print('Перегляд перших 5 рядків даних:')
print(attitude.head())

# перевіряємо наявність пропущених даних
print("Пропущені данні:")
print(attitude.isnull().sum())

# статистика описових характеристик
print('Опис данних:')
print(attitude.describe())

# виконуємо кореляційний аналіз
print('Кореляція:')
print(attitude.corr())

# встановлюємо цільову змінну та факторні змінні
target_var = 'rating'
predictor_vars = ['complaints', 'privileges', 'learning', 'raises', 'critical', 'advance']

# побудова графіків розкиду
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
for predictor, ax in zip(predictor_vars, axs.flat):
    ax.scatter(attitude[predictor], attitude['rating'])
    ax.set_xlabel(predictor.upper())
    ax.set_ylabel('Rating')

plt.show()

fig, axs = plt.subplots(2, 3, figsize=(12, 8))
# побудова моделей парної лінійної регресії для кожної факторної змінної
for predictor, ax in zip(predictor_vars, axs.flat):
    model = smf.ols(f"{target_var} ~ {predictor}", data=attitude).fit()
    print(f"Linear Regression Model for {target_var} ~ {predictor}:")
    print(model.summary())
    ax.scatter(attitude[predictor], attitude['rating'])
    ax.plot(attitude[predictor], model.predict(attitude[predictor]), color='red')
    ax.set_xlabel(predictor.upper())
    ax.set_ylabel('Rating')
plt.show()

# Побудова моделей множинної регресії для різних комбінацій факторних змінних
model1 = smf.ols("rating ~ privileges + raises", data=attitude).fit()
model2 = smf.ols("rating ~ learning + advance", data=attitude).fit()
model3 = smf.ols("rating ~ complaints + critical + advance", data=attitude).fit()
model4 = smf.ols("rating ~ complaints + learning + raises + critical + advance", data=attitude).fit()
model5 = smf.ols("rating ~ complaints + learning", data=attitude).fit()

print(f"Multiple Regression Model for {target_var} ~ complaints + privileges + learning + raises + critical + advance:")
print(model1.summary())
print(f"Multiple Regression Model for {target_var} ~ privileges + critical:")
print(model1.summary())
print(f"Multiple Regression Model for {target_var} ~ learning + critical:")
print(model2.summary())
print(f"Multiple Regression Model for {target_var} ~ complaints + critical + advance:")
print(model3.summary())
print(f"Multiple Regression Model for {target_var} ~ complaints + learning:")
print(model5.summary())
