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


import numpy as np

# a = np.array([0, 1])
# print(a)
#
# a = np.arange(2)  # Sekwencja elementów do umieszczenia w tablicy
# print(a)
# print(type(a))  # Typ
#
# print(a.dtype)  # Typ elementów
#
# a = np.arange(2, dtype='int32')  # Zamień typ elementów na inny
# print(a.dtype)
# b = a.astype('float')  # Utwór tabelę b na podstawie a i zamien na typ float
# print(b)
# print(b.dtype)
# print(b.shape)  # Rozmiar tworzonej tablicy
#
# print(a.ndim)  # Pokaż ilość wymiarów
#
# m = np.array((np.arange(2), np.arange(2)))  # Stwórz tablicę z dwoma wymiarami z dwoma elementami za pomocą arange.
# print(m.shape)
# print(m.ndim)
# m2 = np.array([[2, 3, 5], [2, 8, 6]])
# print(m2)
# print(m2.shape)
# print(m2.ndim)
# print(m2.dtype)
#
# wektor = np.arange(5)
# print(wektor)

# zera = np.zeros((5, 5))
# jedynki = np.ones((4, 4))
# print(zera)
# print(jedynki)
# print(zera.dtype)
# print(jedynki.dtype)
#
# pusta = np.empty((2, 2))
# print(pusta)
# poz_1 = pusta[1, 1]
# poz_2 = pusta[0, 1]
# print(poz_1)
# print(poz_2)
#
# macierz = np.array([[1, 2],
#                     [3, 4],
#                     [2, 5]])
# print(macierz)
# liczby = np.arange(1, 2, 0.1)
# print(liczby)
#
# liczby_lin = np.linspace(1, 2, 5, endpoint=False)
# <początek, koniec, kroków> z endpoint=False przedział z prawej strony jest otwarty
# print(liczby_lin)

# z = np.indices((5, 3))  # Tworzy dwie macierze o wymiarze 5,3
# print(z)
# print(z[0])
# print(z[0, 3, 1])  # Pokaż numer z pierwszej tabeli w trzecim wierszu pierwszej kolumny
# x, y = np.mgrid[0:5, 0:5]  # Stwórz macierz o wymiarze 5x5
# print(x)
# print(y)
# print("Stwórz macierz diagnogalną")
# mat_diag_k = np.diag([a for a in range(5)])  # Stwórz macierz diagnogalną
# mat_diag_k2 = np.diag([a for a in range(5)], k=-1)  # Stwórz macierz diagnogalną o jeden niżej
# print(mat_diag_k)
# print(mat_diag_k2)

# z = np.fromiter(range(5), dtype='int32')  # Tworzy tablicę jednowymiarową, wektor z 5-cioma elementami
# print(z)

# znaki = b'abcdef'  # b'' jako ciąg bajtów
# zn1 = np.frombuffer(znaki, dtype='S1')  # S1 ilośc elementów o długości 1 z bufora znaki
# print(zn1)
# zn2 = np.frombuffer(znaki, dtype='S2')  # S2 Po dwóch znakach jako pierwszy element
# print(zn2)

# S1 = String z dokładanym ilością znaku
# U1 = Unicode (Unikowy)

# znaki = 'abcdef'
# zn3 = np.array(list(znaki))
# zn4 = np.array(list(znaki), dtype='S1')
# zn5 = np.array(list(b'abcdef'))  # Jako kod ASCII gdy podstawiamy b przed stringiem
# zn6 = np.fromiter(znaki, dtype='S1')
# zn7 = np.fromiter(znaki, dtype='U1')  # Kasowany jest przedrostek b
# print(zn3)
# print(zn4)
# print(zn5)
# print(zn6)
# print(zn7)


# DZIAŁANIA MATEMATYCZNE NA TABLICY

# mat = np.ones((2, 2))
# mat_1 = np.ones((2, 2))
# mat = mat+mat_1
# print(mat)
# print(mat - mat_1)
# print(mat * mat_1)
# print(mat / mat_1)
# mat_1 = np.array([[3, 5], [5, 4]])
# print(mat_1)
# print(mat*mat_1)
# print(mat/mat_1)

# BRANIA INFORMACJI Z MACIERZY/WEKTORÓW

# a = np.arange(10)
# print(a)
# s = slice(2, 7, 2)
# print(a[s])
# s = range(2, 7, 2)
# print(a[s])
# print(a[2:7:2])  # Indeks początkowy:końcowy:odstępy
# print(a[1:])  # Wyświetl wszystko od początku do końca
# print(a[2:5])  # Wyświetl tablicę z indeksem od miejsca 2 do 5

# mat = np.arange(25)
# mat = mat.reshape((5, 5))
# print(mat)
# print(mat[1:])
# print(mat[:, 1])  # Jako wektor
# print(mat[:, -1:])  #
# print(mat[2:6, 1:3])  # Pokaż fragment 3x2
# print(mat[:, range(2, 6, 2)])  # Wycięcie po kolumnach
# print('')
#

# NIESTANDARDOWY PRZYKŁAD CIĘCIA

# x = np.array([[0, 1, 2],
#              [3, 4, 5],
#              [6, 7, 8],
#              [9, 10, 11]])
# print(x)
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
# y = x[rows, cols]
# print(y)
