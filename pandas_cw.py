import pandas as pd
import numpy as np
s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# print()
s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
# print(s)
# print()
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
# print(df)
# print(df.dtypes)
# # df = pd.read_csv('dane.csv', header=0, sep=";", decimal=',')  # Wczytaj plik CSV (Decimal decyduje
# #                                                                 o separator liczb dziesiętnych, header decyduje o
# #                                                                 ułożenie danych)
# # df.to_csv('plik.csv', index=False)  # Zapisz do CSV. Mając Index na False wyłączy specyikacje wierszy
# print()
# print(s['c'])
# print(s.a)
# print(df[0:1])
# print('')
# print(df['Populacja'])  # Pokaż wartośc w kluczu Populacja
# print(df.iloc[0, 0])  # Pokaż położenie 1x1
# print(df.loc[0, "Kraj"])  # Pokaż położenie 1 w słowniku Kraj
# print(df.at[0, "Populacja"])  # Pokaż położenie 1 w słowniku Populacja
# print()
#
# print('kraj: ' + df.Kraj)  # Do każdego elementu z kolumny kraj jest dopisany ciąg elementu 'kraj:'
# print()
# print(df.sample())  # Wybór wierszy z ramki (z 1 elementu)
# print()
# print(df.sample(2))  # tj. tyle że z 2 elementów
# print()
# print(df.sample(frac=0.5))  # Przy wartości procentowej, w tym przypadku 50%
# print()
# print(df.sample(n=10, replace=True))  # Możliwośc powtarzania wierszy
# print()
# print(df.head())  # Pokaż 5 (domyślnie) początkowych
# print()
# print(df.head(2))
# print()
# print(df.tail(1))
# print("\ndf.tail():")
# print(df.tail())  # Pokaż 5 (domyślnie) ostatnich
# print()
# print(df.describe())
# print()
# print(df.T)  # Transponowanie ramki danych

# print(s[(s > 9)])
# print(s.where(s > 10))
# print(s.where(s > 10, 'za duże'))
# seria = s.copy()
# seria.where(seria > 10, 'za duże', inplace=True)
# print('########')
# print(seria)
#
# print(s[~(s > 10)])
#
# print(s[(s < 13) & (s > 8)])

# print(df[(df.Populacja > 1000000) & (df.index.isin([0, 2]))])
# print('########')
# szukaj = ['Belgia', 'Brasilia']
# print(df.isin(szukaj))

# WSTAWIANIE WARTOŚCI #
# tablica[nazwa indeksu] = wartość
# s['e'] = 15
# print(s.e)
# s['f'] = 16
# print(s)

# Dodawanie elementu do ramki danych
df.loc[3] = 'Dodane'
print(df, end='\n\n')
# Wg. indeksu KRAJ STOLICA POPULACJA
df.loc[4] = ['Polska', 'Warszawa', 38675467]
print(df, end='\n\n')
new_df = df.drop([3])
print(new_df, end='\n\n')
df.drop([3], inplace=True)
print(df, end='\n\n')
# df.drop('Kraj', axis=1, inplace=True)  # Mając axis na 1 usuwa kolumny. Przy 0 (domyslnie) usuwa wiersz.
# print(df)
# DODAWANIE WIERSZY DO RAMKI #
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
print(df, end='\n\n')
print(df.sort_values(by='Kraj'), end='\n\n')
grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa',), end='\n\n')
print(df.groupby(['Kontynent']).agg({'Populacja': ['sum']}), end='\n\n')  # Stwórz grupę z agregacją
print(df.groupby(['Kontynent']).agg('Populacja').sum())