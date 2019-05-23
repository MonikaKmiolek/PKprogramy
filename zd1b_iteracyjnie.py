print("Wypisz liczby do spotęgownaia:")
def potegowanie(x, n):
    x = int(input('podaj wartość x: '))
    n = int(input('podaj wartość n: '))
    if n == 0:
        print(1)
    elif n > 0:
        print(x*x**(n-1))
    elif n < 0:
        print(1/(x**n))

    return