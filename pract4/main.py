import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.stats import ttest_1samp

file = pd.read_csv("airquality.csv")
df = pd.DataFrame(file)
print(df.head())
print("Наявність пропущених даних: " + str(df.isnull().values.any()))

df = df.fillna(df.mean().round(1))
print(df.head())
print("Наявність пропущених даних: " + str(df.isnull().values.any()))

plt.figure()
df['Temp'].plot()
plt.figure()
df['Temp'].hist()
plt.figure(figsize=(2, 1))
df['Temp'].hist(by=pd.to_datetime(df['Month'], format='%m').dt.strftime('%B'))
plt.suptitle('Temperature Distribution by Month', fontsize=20, y=5)
plt.subplots_adjust(hspace=1.5)

for ax in plt.gcf().axes:
    ax.set_xlabel('Temperature (°F)', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)

    ax.title.set_fontsize(14)
    ax.title.set_y(1.05)
plt.show()

emp_mean = df['Temp'].mean()
emp_std = df['Temp'].std()
print("Емпіричне середнє: ", emp_mean)
print("Емпіричне середньоквадратичне відхилення: ", emp_std)


mu = 77
sigma = 10

t_stat, p_value = ttest_1samp(df['Temp'], mu)

if p_value < 0.05:
    print("Відхилення нульової гіпотези")
else:
    print("Нульова гіпотеза не відхилена")

conf_int = st.t.interval(alpha=0.90, df=len(df['Temp'])-1,
              loc=np.mean(df['Temp']),
              scale=st.sem(df['Temp']))

print('Довірчий інтервал: ' + str(conf_int))
