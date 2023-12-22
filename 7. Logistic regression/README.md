# Task 7. Logistic regression

### 1. Exploratory data analysis

For the set of attributes that are highlighted in blue:\
Briefly describe the presented data set:

- features of distributions, limits of variation, means, medians, correlations, etc. Draw a histogram of the of the
  distribution.
- Compare groups with Paid and Charge off loan status (variable "status_on_close"). Display the results visually the
  results of the comparison on a graph (you choose the type of graph yourself).
  Is there a significant difference between them by any of the features of the data available in the sample? Give
  reasonable conclusions.
- Compare groups by age: under 35 and over 35. Display the comparison visually. Is there a significant difference
  between them on any of the features of the data available in the sample?
  Show the differences visually on a graph (the type of graph is up to you). (Age can be defined as the difference
  between the date of birth and the date of death. as the difference between the date of birth and
  application__created_date).
- Print the top 10 car brands.

### 2. Modeling.

For the set of attributes highlighted in gray:

- Build a model No. 1 that will give a score for the borrower - the probability of repaying the loan.
- Build model No. 2 by adding information about the borrower's age and income to model No. 1.

***Note***:
In all models, use the indicator named flg_income as the dependent variable.
Dependent quantitative variables should be categorized as categorical variables. The number of categories should be 2 - 6.\
To select independent variables - predictors - use some type of selection (forward, backward, stepwise) - justify your
choice.
Analyze the selected variables. Evaluate the effectiveness of the built model. What indicators/statistics can be used
for this purpose. Compare all the models you have built according to these criteria.

# Завдання 7. Логістична регресія

### 1. Розвідувальний аналіз даних\

Для набору атрибутів, які виділені блакитним кольором:\
Коротко описати представлений набір даних:

- особливості розподілів, межі зміни величин, середні, медіани, кореляції тощо. Побудувати гістограму
  розподілу.
- Порівняти групи з Paid та Charge off loan статусом (змінна “status_on_close”). Відобразити візуально
  результати порівняння на графіку (тип графіка вибираємо самостійно).\
  Чи суттєва відмінність між ними за якоюсь із ознак доступних у вибірці даних? Дати обґрунтовані
  висновки.
- Порівняти групи за віком: до 35 та старше 35 років. Відобразити порівняння візуально.
  Чи суттєва відмінність між ними за якоюсь із ознак доступних у вибірці даних?
  Відобразити відмінності візуально на графіку (тип графіка вибираємо самостійно). (вік можна визначити
  як різницю між датою народження та application__created_date).
- Вивести топ-10 марок автомобілів.

### 2. Моделювання

Для набору атрибутів, виділених сірим кольором:

- Побудуйте модель No 1, яка дасть оцінку позичальнику - ймовірність того, чи виплатить він кредит.
- Побудуйте модель No 2, додавши в модель No 1 інформацію про вік та доходи позичальника.

***Примітка***:
У всіх моделях використовуйте індикатор з ім'ям flg_income як залежну змінну.
Залежні кількісні змінні необхідно розбити на групи – і їх як категоріальні. Кількість категорій має бути 2
– 6.\
Для відбору незалежних змінних – предикторів – використовуйте якийсь тип selection (forward,
backward, stepwise) – аргументуйте свій вибір.\
Проведіть аналіз відібраних змінних. Дайте/наведіть оцінку ефективності побудованої моделі. Які
показники/статистики для цього можна використати. Порівняйте між собою всі побудовані вами моделі
за цими критеріями.\