import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()  # Stwórz wykres tekstowy
# plt.show()  # Stwórz wykres rysunkowy

#  WYKRES SŁUPKOWY  #
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}
df = pd.DataFrame(data)
print(df)
# PIERWSZY SPOSÓB
grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
print(grupa)
grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Mld', rot=0,
           legend=True, title='Populacja z podziałem na kontynenty')
# DRUGI SPOSÓB #
wykres = grupa.plot.bar()
wykres.set_ylabel('Mld')
wykres.set_xlabel('Kontynent')
wykres.tick_params(axis='x', labelrotation=0)
wykres.legend()
wykres.set_title('Populacja z podziałem na kontynenty')
# plt.xticks(rotation=0)
plt.savefig('wykres.png')
plt.show()
