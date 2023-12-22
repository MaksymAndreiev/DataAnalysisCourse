import matplotlib.pyplot as plt
import pandas as pd

diamonds = pd.read_csv("diamonds.csv")
print(diamonds.dtypes)
print(diamonds.head(n=10))

price = diamonds["price"]
carats = diamonds["carat"]
cut = diamonds['cut']
color = diamonds['color']
clarity = diamonds['clarity']

print('Середня вага діамантів:')
print(carats.mean())
print('Середня ціна:')
print(price.mean())
print('Максимальна ціна:')
print(price.max())
print('Мінімальна ціна:')
print(price.min())

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

axs[0, 0].hist(carats)
axs[0, 0].set_xlabel('Вага діаманта (карат)')
axs[0, 0].set_ylabel('Частота')
axs[0, 0].set_title('Розподіл ваги діамантів')

axs[0, 1].hist(cut)
axs[0, 1].set_xlabel('Різновидість')
axs[0, 1].set_ylabel('Частота')
axs[0, 1].set_title('Розподіл різновидностей')

axs[1, 0].hist(color)
axs[1, 0].set_xlabel('Колір')
axs[1, 0].set_ylabel('Частота')
axs[1, 0].set_title('Розподіл кольорів діамантів')

axs[1, 1].hist(clarity)
axs[1, 1].set_xlabel('Чистота')
axs[1, 1].set_ylabel('Частота')
axs[1, 1].set_title('Розподіл чистоти діамантів')

plt.tight_layout()
plt.show()


print("Таблиця частот для змінної cut")
cut_freq = pd.crosstab(index=cut, columns='count')
print(cut_freq)

print("Таблиця частот для змінної color")
color_freq = pd.crosstab(index=color, columns='count')
print(color_freq)

print("Таблиця частот для змінної clarity")
clarity_freq = pd.crosstab(index=clarity, columns='count')
print(clarity_freq)

# Розрахунок величини загальної глибини у відсотках
print("Розрахунок величини загальної глибини у відсотках")
depth_percent = ((diamonds["z"] / ((diamonds['x'] + diamonds['y']) / 2)) * 100).mean()
print(depth_percent)
