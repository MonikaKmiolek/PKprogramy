import math


def rekurencja(x, n):
    if n == 0:
        return 1
    elif n>0:
        return x*rekurencja(x,n-1)
    elif n<0:
        return 1/(x*rekurencja(x,-n-1))
    else:
        print("Nie podano prawidłowych wartości")

#przykład użycia 1
#    wynik1=rekurencja(x, n)
#    print(wynik1)

#przykład użycia 2
#try:
#    x=float(input("Podaj liczbę do spotęgowania:"))
#    n=int(input("Podaj potęgę:"))
#    wynik2 = rekurencja(x, n)
#    print(wynik2)
#except:
#    print("Nie podano prawidłowych wartości")

