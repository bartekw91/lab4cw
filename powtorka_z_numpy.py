import numpy as np

a = np.array([20, 30, 40, 50])  # Stwórz wektor z własnymi liczbami
b = np.arange(4)  # Stwórz wektor od 0 do 3
print(a)
print(b)

c = a - b  # Odejmujemy wektory (liczba indeksów musi byc taka sama)
print(c)

print(b**2)  # Podnosimy wektory do potęgi 2

print(a)
a += b
print(a)
a -= b
print(a)

d = np.arange(3)
print()
print(d)
print(np.exp(d))
print(np.sqrt(d))
e = np.array([2., -1., 4.])
print(np.add(d, e))
print()

f = a*b
print(f)
print(a.dot(b))  # Mnożenie macierzy o tych samych WxK
g = np.array([[1, 5], [2, 6], [7, 4]])
h = np.array([[2, 5, 4], [4, 3, 1]])
print(g)
print(h)
print(np.dot(g, h))  # Mnożenie macierzy
print(np.dot(h, g))
print()
i = np.arange(12).reshape(3,4)  # Stwórz wektor od 0 do 11 i zamień na macierz 3x4
print(i)
print(i.sum())  # Sumuj wszystkie macierzy
print(i.sum(axis=0))  # Sumuj liczby po kolumnie
print(i.min(axis=1))  # Pokaż najmniejsze liczby poszczególnych macierzy przy każdym wierszu
print(i.cumsum(axis=1))  # Skumulowana suma elementów
print()
j = np.arange(6).reshape((3, 2))
print(j)
print()
for q in j:  # Element q będzie jako pojedyńczy wiersz
    print(q)
print()
for q in j.flat:  # Spłaszczenie do wektora
    print(q)
print()
#for q in j:
#    for r in range(len(j)):  # Dostęp do każdego elementu z wierszy
#        print(q[r], end=' ')
print()
#for q in range(0, j.shape[0]):
#    for w in range(0, a.shape[1]):
#        print(j[q][w], end=' ') # Dostęp do poszczególnego elementu WxK
#        print(' ')

print('PRZEKSZTAŁCENIE')
k = np.arange(6)
print(k)
print(k.shape)
print('')
l = k.reshape((2, 3))
print(l)
print(l.shape)
print('')
m = l.reshape((3, 2))
print(m)
print(m.shape)
print('')
n = m.ravel()  # Spłaszcz macierz do postaci wektora
print(n)
print(n.shape)
print('')
o = l.T   # Transponowanie
print(o)
print(o.shape)
