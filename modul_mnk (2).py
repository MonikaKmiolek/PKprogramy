import numpy as np

def gen_ur_mnk(X, Y, st):
    A = np.zeros((st + 1, st + 1))
    B = np.zeros((st + 1,))

    n = len(X)  # liczba elemntów w wektorze x
    XX = [1.0 for i in range(n)]  # tworzymy liste jedynek ile elementów w wektorze x
    print("XX:", XX)
    XY = [Y[i] for i in range(n)]  # pod nią wprowadzamy wartości y, po to by pozniej móc je potegować
    print("XY:", XY)
    # Czyli for i in range(n):
    #           XY.append(Y[i])

    # WYPEŁNIENIE GÓRNEGO TRÓJKĄTA #rozbijamy macierz na dwa trojkąty: trójkąt górny i antytrojkat
    for i in range(st + 1):
        # W wektorze XX pamiętamy bieżące potęgi wszystkich x. Sumujemy je,
        # po czym zwiększamy daną potęgę o 1.
        # Pod A w wierszu zerowym, kolumnie i wstawiamy sumę XX i czyli na
        # razie wypełniamy macierz A tylko poszczególnymi potęgami x-ów
        # i TYLKO W PIERWSZYM WIERSZU
        A[0, i] = sum(XX)
        print("A1:", A)
        # Z kolei w macierzy B wypełniamy poszczególne wiersze sumami
        # zmiennych y
        B[i] = sum(XY)
        print("B:", B)
        print("\n")
        # Propagacja wartości wzdłuż linii 'w lewo w dół'
        # i - ta kolumna
        for j in range(i):
            # j+1 - schodzimy do wiersza niżej (następnego)
            # i-j-1 - zaczynając od kolumny i  przechodzimy do poprzedniej,
            # kolejnej poprzedniej i kolejnej, dopóki nie dojdziemy do
            # pierwszej kolumny
            A[j + 1, i - j - 1] = A[0, i]
        print("A2:", A)
        # po czym zwiększamy stopień potęgi o 1 - aktualizacja XX, YY

        print("\n")

        # Teraz mnożymy każdą z potęg przez daną zmienną x
        # n jest mniejsze od stopienWielomianu+1, czyli jedna z kolumn nie
        # zostanie przemnożona - czy nie wychodzi na to, że nie zostanie
        # przemnożona ostatnia, kiedy powinna być to pierwsza?
        for j in range(n):
            XX[j] *= X[j]
            XY[j] *= X[j]

        print("XX:", XX)
        print("XY:", XY)

    print("\n")

    # WYPEŁNIENIE DOLNE
    for i in range(1, st + 1):
        A[i, st] = sum(XX)
        # propagacja 'w lewo dol az do ostatniego wiersza'
        for j in range(i + 1, st + 1):
            A[j, st + i - j] = A[i, st]
        for j in range(n):
            XX[j] *= X[j]

    #wsp = np.linalg.solve(A, B) # a0,a1,a2
    #print('wsp:', wsp)

    return A,B

                    # def wsp(a,b):
                    #     wsp = np.linalg.solve(a, b) # a0,a1,a2
                    #     print('wsp:', wsp)
                    #     return wsp

def wielomian1(x, wsp):
    w = 0.0
    # wsp - wektor współczynników
    for i in range(len(wsp)):
        w += wsp[i] * x ** i

    return w

def wielomian2(x, wsp):
    w = wsp[-1]
    # i powinno się zacząć od wartości mnniejszej o 1 od st
    for i in range(len(wsp)-2, -1, -1):
        print(i, wsp[i])
        w = w*x + wsp[i]

    return w

def r_kwadrat(y,f):
    for (p, q) in zip(y, f):  # łączenie w pary x i y
        print(p, q)

    ysr = (sum(y))/(len(y))
    L = 0
    M = 0
    for i in range(len(f)):
        L = L + ((y[i]) - (f[i]))**2
    for i in y:
        M = M + (i - ysr)**2
    print('Współczynnik determinacji:',(1 - (L/M)))
    return 1 - (L/M)

def blad(y,f):
    L = 0
    for i in range(len(f)):
        L = L + ((y[i]) - (f[i]))**2
    print('Błąd średniokwadratowy:',L)
    return L




