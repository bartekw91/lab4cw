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
