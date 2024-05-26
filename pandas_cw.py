import pandas as pd
import numpy as np
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
print()
s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)
print()
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=',')  # Wczytaj plik CSV (Decimal decyduje
#                                                                 o separator liczb dziesiętnych, header decyduje o
#                                                                 ułożenie danych)
# df.to_csv('plik.csv', index=False)  # Zapisz do CSV. Mając Index na False wyłączy specyikacje wierszy
print()
print(s['c'])
print(s.c)
print(df[0:1])
print('')
print(df['Populacja'])  # Pokaż wartośc w kluczu Populacja
print(df.iloc[0, 0])  # Pokaż położenie 1x1
print(df.loc[0, "Kraj"])  # Pokaż położenie 1 w słowniku Kraj
print(df.at[0, "Populacja"])  # Pokaż położenie 1 w słowniku Populacja

