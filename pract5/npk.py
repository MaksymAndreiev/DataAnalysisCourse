import pandas as pd
from scipy.stats import f_oneway

data = pd.read_csv('npk.csv')

group_n = data.groupby('N')['yield'].apply(list)
group_p = data.groupby('P')['yield'].apply(list)
group_np = data.groupby(['N', 'P'])['yield'].apply(list)

f_val, p_val = f_oneway(*group_n)
print("N: F =", f_val, ", p1 =", p_val)

f_val, p_val = f_oneway(*group_p)
print("P: F =", f_val, ", p1 =", p_val)

f_val, p_val = f_oneway(*group_np)
print("N x P: F =", f_val, ", p1 =", p_val)
