import matplotlib
import pandas as pd
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

pd.set_option('display.float_format', lambda x: '%.2f' % x)

read_file = pd.read_excel("data_sell_eng.xlsx")
df1 = pd.DataFrame(read_file)

read_file = pd.read_excel("data_sell_eng_2.xlsx")
df = pd.DataFrame(read_file)

df = df1.join(df.set_index('Number_Category'), on='Number_Category')

df['Price_product'] = df['Sale_Amount'] / df['Quantity']
print(df.head())
print(df.columns.values.tolist())

print('\n\n')

print("Кількість")
print('регіонів збуту: ' + str(df['Region'].nunique()))
print('ринків збуту: ' + str(df['Market'].nunique()))
print('штатів: ' + str(df['State'].nunique()))

print('\n\n')

df3 = pd.DataFrame([df['Region'].nunique(), df['Market'].nunique(), df['State'].nunique()],
                   columns=['Amount'], index=['Region', 'Market', 'State'])
print("Таблиця")
print(df3)
print('\n\n')

region_df = df.groupby('Region')[['Quantity', 'Sale_Amount']].sum()
state_df = df.groupby('State')[['Quantity', 'Sale_Amount']].sum()
print("Обсяги продажів та суми за кожним регіоном збуту")
print(region_df)
print('\n\n')
print("Обсяги продажів та суми за кожним штатом")
print(state_df)
print('\n\n')

q_mean = df.groupby('Region')['Quantity'].mean()
q_max = df.groupby('Region')['Quantity'].max()
q_min = df.groupby('Region')['Quantity'].min()
q_sum = df.groupby('Region')['Quantity'].sum()

print("Середнє\n")
print(q_mean)
print("\n\nМаксимум\n")
print(q_max)
print("\n\nМінімум\n")
print(q_min)
print("\n\nСума\n")
print(q_sum)

s_mode = df.groupby('Region')['Sale_Amount'].agg(pd.Series.mode)
s_median = df.groupby('Region')['Sale_Amount'].median()
s_std = df.groupby('Region')['Sale_Amount'].std()

print("\n\nМода\n")
print(s_mode)
print("\n\nМедіана\n")
print(s_median)
print("\n\nДисперсія\n")
print(s_std)

summary_df = pd.concat([q_mean.rename('Mean'), q_max.rename('Max'), q_min.rename('Min'), q_sum.rename('Sum'),
                        s_mode.rename('Mode'), s_median.rename('Median'), s_std.rename('STD')], axis=1)
print('\n\n')
print(summary_df)
summary_df.to_csv(r'..\pract2\result.txt')

cm = matplotlib.colormaps.get_cmap('Set2')
f1 = plt.figure()
ax1 = f1.add_subplot(111)
df['Quantity'].plot(ax=ax1, bins=5, range=[0, 10], legend=False, kind='hist', color=cm.colors)
for i, ax in enumerate(f1.axes):
    k = 0
    ax.grid(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for rect in ax.patches:
        if rect.get_height() > 0 and k < cm.N:
            rect.set_color(cm(k))
            k += 1
plt.ylabel('Frequency')
plt.xlabel('Quantity')
plt.title('Histogram of Quantity')

f2 = plt.figure(figsize=(10, 4))
ax2 = f2.add_subplot(111)
categories = df['Product_Category'].unique()
ax2.bar(range(len(categories)), df.groupby('Product_Category')['Quantity'].sum(), color=cm.colors)
ax2.tick_params(axis='both', which='minor', labelsize=2)
plt.xticks(range(len(categories)))
ax2.set_xticklabels(categories, fontsize=5)
plt.ylabel('Quantity')
plt.xlabel('Product Category')
plt.title('Bar Chart of Quantity by Product Category')
plt.show()
