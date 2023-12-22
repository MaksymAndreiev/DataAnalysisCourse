import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Максим Андреєв - LungCapData.csv')

corr = df.corr(numeric_only=True)
print(corr)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Кореляція між метричними ознаками')
plt.show()

