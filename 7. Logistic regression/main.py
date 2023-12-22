import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import MatplotlibDeprecationWarning
from scipy.stats import ttest_ind
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore",
                        message="Support for FigureCanvases without a required_interactive_framework attribute was "
                                "deprecated in Matplotlib 3.6",
                        category=MatplotlibDeprecationWarning)
warnings.filterwarnings("ignore", message="A value is trying to be set on a copy of a slice from a DataFrame")

# Завантаження даних
data = pd.read_csv('for_MODEL.csv')

print('-' * 80)
print('Наявність пустих рядків:')
print(data.isnull().sum())
print('*' * 80)

data.replace('N/A', np.nan, inplace=True)

# загальна кількість NaN значень у даних
total_nans = data.isna().sum().sum()
print(f'Кількість пустих та не валідних даних (разом): {total_nans}')

data = data.dropna()

print('-' * 80)
print('Наявність пустих рядків:')
print(data.isnull().sum())
print('*' * 80)
total_nans = data.isna().sum().sum()
print(f'Кількість пустих та не валідних даних (разом): {total_nans}')

pd.options.display.max_columns = data.shape[1]
blue_data = data.iloc[:, :11]
gray_data = data.iloc[:, 11:]

# Опис даних
print('-' * 80)
print('Опис даних')
print('-' * 80)
print(blue_data.describe(include='all'))
print('.' * 80)

numeric_cols = blue_data.select_dtypes(include=np.number)

# Кореляційна матриця
print('-' * 80)
print('Кореляційна матриця')
print('-' * 80)
corr_matrix = numeric_cols.corr()
print(corr_matrix)
print('.' * 80)

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.title('Кореляція')

fig, axs = plt.subplots(2, 3, figsize=(12, 8))
for column, ax in zip(numeric_cols, axs.flat):
    # Побудова гістограми розподілу
    ax.hist(blue_data[column], bins=20)
    ax.set_xlabel(column)
    ax.set_ylabel('Частота')

blue_data = data.loc[data['status_on_close'].isin(['Paid', 'Chargeoff'])]

paid = blue_data[blue_data['status_on_close'] == 'Paid']
charge_off = blue_data[blue_data['status_on_close'] == 'Chargeoff']

t_statistic, p_value = ttest_ind(paid['monthly_earnings'], charge_off['monthly_earnings'], equal_var=False)
print('t-критерій для місячних доходів:', t_statistic)
print('p-значення для місячних доходів:', p_value)

t_statistic, p_value = ttest_ind(paid['fico'], charge_off['fico'], equal_var=False)
print('t-критерій для fico:', t_statistic)
print('p-значення для fico:', p_value)

t_statistic, p_value = ttest_ind(paid['MBSCORE'], charge_off['MBSCORE'], equal_var=False)
print('t-критерій для MBSCORE:', t_statistic)
print('p-значення для MBSCORE:', p_value)

t_statistic, p_value = ttest_ind(paid['term'], charge_off['term'], equal_var=False)
print('t-критерій для строку кредиту:', t_statistic)
print('p-значення для строку кредиту:', p_value)

t_statistic, p_value = ttest_ind(paid['selling_price'], charge_off['selling_price'], equal_var=False)
print('t-критерій для ціни продажу автомобіля:', t_statistic)
print('p-значення для ціни продажу автомобіля:', p_value)

plt.figure()
plt.hist([paid['status_on_close'], charge_off['status_on_close']], bins=1, label=['Сплачено', 'Не виконано зобов\'язань'])
plt.xlabel('Статус кредиту')
plt.ylabel('Кількість кредитів')
plt.title('Розподіл статусу кредитів')
plt.legend()

# Графік місячних доходів
fig, ax = plt.subplots()
ax.boxplot([paid['monthly_earnings'], charge_off['monthly_earnings']])
ax.set_xticklabels(['Сплачено', 'Не виконано зобов\'язань'])
ax.set_title('Порівняння щомісячного доходу між статусами кредитів')
ax.set_ylabel('Щомісячний дохід')
ax.set_xlabel('Статус кредиту')
plt.show()

# Графік показника FICO
fig, ax = plt.subplots()
ax.boxplot([paid['fico'], charge_off['fico']])
ax.set_xticklabels(['Сплачено', 'Не виконано зобов\'язань'])
ax.set_title('Порівняння показника FICO між статусами кредитів')
ax.set_ylabel('FICO')
ax.set_xlabel('Статус кредиту')
plt.show()

# Графік показника MBSCORE
fig, ax = plt.subplots()
ax.boxplot([paid['MBSCORE'], charge_off['MBSCORE']])
ax.set_xticklabels(['Сплачено', 'Не виконано зобов\'язань'])
ax.set_title('Порівняння показника MBSCORE між статусами кредитів')
ax.set_ylabel('MBSCORE')
ax.set_xlabel('Статус кредиту')
plt.show()

# Графік строку кредиту
fig, ax = plt.subplots()
ax.boxplot([paid['term'], charge_off['term']])
ax.set_xticklabels(['Сплачено', 'Не виконано зобов\'язань'])
ax.set_title('Порівняння строку кредиту між статусами кредитів')
ax.set_ylabel('Строк кредиту')
ax.set_xlabel('Статус кредиту')
plt.show()

# Графік ціни продажу автомобіля
fig, ax = plt.subplots()
ax.boxplot([paid['selling_price'], charge_off['selling_price']])
ax.set_xticklabels(['Сплачено', 'Не виконано зобов\'язань'])
ax.set_title('Порівняння ціни продажу автомобіля між статусами кредитів')
ax.set_ylabel('Ціна продажу автомобіля')
ax.set_xlabel('Статус кредиту')
plt.show()

dob = pd.to_datetime(blue_data['dob'], format='%m/%d/%Y')
acd = pd.to_datetime(blue_data['application__created_date'], format='%d/%m/%Y')
blue_data['age'] = (acd - dob) / pd.to_timedelta(365.25, unit='D')

# Розділення груп за віком
under35 = blue_data[blue_data['age'] < 35]
over35 = blue_data[blue_data['age'] >= 35]

# порівняння груп за ознакою "місячний дохід"
t_statistic, p_value = ttest_ind(under35['monthly_earnings'], over35['monthly_earnings'], equal_var=False)
print('t-критерій для місячних доходів:', t_statistic)
print('p-значення для місячних доходів:', p_value)

# порівняння груп за ознакою "MBSCORE"
t_statistic, p_value = ttest_ind(under35['MBSCORE'], over35['MBSCORE'], equal_var=False)
print('t-критерій для MBSCORE:', t_statistic)
print('p-значення для MBSCORE:', p_value)

# порівняння груп за ознакою "ціна продажу автомобіля"
t_statistic, p_value = ttest_ind(under35['selling_price'], over35['selling_price'], equal_var=False)
print('t-критерій для ціни продажу автомобіля:', t_statistic)
print('p-значення для ціни продажу автомобіля:', p_value)

# порівняння груп за ознакою "термін кредиту"
t_statistic, p_value = ttest_ind(under35['term'], over35['term'], equal_var=False)
print('t-критерій для терміну кредиту:', t_statistic)
print('p-значення для терміну кредиту:', p_value)

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot([under35['monthly_earnings'], over35['monthly_earnings']])
ax.set_xticklabels(['<35', '>=35'])
ax.set_title('Порівняння місячних доходів між віковими групами')
ax.set_ylabel('Місячні доходи')

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot([under35['fico'], over35['fico']])
ax.set_xticklabels(['<35', '>=35'])
ax.set_title('Порівняння значень fico між віковими групами')
ax.set_ylabel('fico')

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot([under35['vehicle_age'], over35['vehicle_age']])
ax.set_xticklabels(['<35', '>=35'])
ax.set_title('Порівняння віку автомобіля між віковими групами')
ax.set_ylabel('Вік автомобіля (у роках)')

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot([under35['term'], over35['term']])
ax.set_xticklabels(['<35', '>=35'])
ax.set_title('Порівняння строку кредиту між віковими групами')
ax.set_ylabel('Строк кредиту (у місяцях)')

plt.show()

# виведення топ-10 марок автомобілів
print('-' * 80)
print('Топ-10 марок автомобіля')
print('-' * 80)
top_10_brands = data['vehicle_make'].value_counts().head(10)
print(top_10_brands)
print('.' * 80)

numeric_cols = gray_data.applymap(pd.to_numeric, errors='coerce')
numeric_cols = numeric_cols.select_dtypes(include=np.number)
numeric_cols = numeric_cols.dropna(axis=1, how='all')
numeric_cols = numeric_cols.dropna()
for column in numeric_cols:
    numeric_cols[column] = pd.cut(numeric_cols[column], bins=2, labels=[0, 1])

cols_to_update = numeric_cols.drop("flg_income", axis=1)
gray_data[cols_to_update.columns] = cols_to_update
gray_data.update(numeric_cols)
gray_data['nameAddressMatch'] = gray_data['nameAddressMatch'].replace({'Y': 1, 'N': 0})

# Розділення даних на навчальну і тестову вибірки
train_data, test_data, train_target, test_target = train_test_split(gray_data.drop('flg_income', axis=1),
                                                                    gray_data['flg_income'],
                                                                    test_size=0.2,
                                                                    random_state=42)

# Створення моделі логістичної регресії
model1 = LogisticRegression()

# Відбір змінних за допомогою backward selection
selector = RFECV(estimator=model1, step=1, cv=5)
selector.fit(train_data, train_target)

# Вибір найкращих змінних
selected_features = train_data.columns[selector.support_]

# Оновлення даних для використання тільки найкращих змінних
train_data = train_data[selected_features]
test_data = test_data[selected_features]

# Навчання моделі на навчальній вибірці
model1.fit(train_data, train_target)

# Оцінка точності моделі на тестовій вибірці
accuracy = model1.score(test_data, test_target)
print("Точність:", accuracy)

# Обчислення матриці помилок на тестовій вибірці
accuracy = model1.score(test_data, test_target)
R_squared = accuracy ** 2
print(R_squared)

gray_data = pd.concat([gray_data, blue_data[['age', 'monthly_earnings']]], axis=1)
gray_data = gray_data.dropna()

# Розділення даних на навчальну і тестову вибірки
train_data, test_data, train_target, test_target = train_test_split(gray_data.drop('flg_income', axis=1),
                                                                    gray_data['flg_income'],
                                                                    test_size=0.2,
                                                                    random_state=42)
# Створення моделі логістичної регресії
model2 = LogisticRegression(max_iter=10000)

# Відбір змінних за допомогою backward selection
selector = RFECV(estimator=model2, step=1, cv=5)
selector.fit(train_data, train_target)

# Вибір найкращих змінних
selected_features = train_data.columns[selector.support_]

# Оновлення даних для використання тільки найкращих змінних
train_data = train_data[selected_features]
test_data = test_data[selected_features]

# Навчання моделі на навчальній вибірці
model2.fit(train_data, train_target)

# Оцінка точності моделі на тестовій вибірці
accuracy = model2.score(test_data, test_target)
print("Точність:", accuracy)

# Обчислення матриці помилок на тестовій вибірці
accuracy = model2.score(test_data, test_target)
R_squared = accuracy ** 2
print(R_squared)
