import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)

# grupa = (df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia': ['sum']}))
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6),
#           colors=['red', 'green'])  # PIERWSZY SPOSÓB
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))  # DRUGI SPOSÓB
# plt.legend(loc='lower right')
# plt.title('Suma Zamówienia Dla Sprzedawcy')
# plt.show()

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
df = pd.DataFrame(ts, columns=['wartości'])
print(df)
df['Średnia krocząca'] = df.rolling(window=25).mean()
df.plot()
plt.legend()
plt.show()
