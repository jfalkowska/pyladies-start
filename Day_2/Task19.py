print()
def moje_dodawanie(a, b):
    c = a + b
    print('Twoim wynikiem jest liczba: ' + str(c))

moje_dodawanie(2, 4)
print()

def moje_potegowanie(a, b=2):
    c = a ** b
    print('Liczba ' + str(a) + ' podniesiona do potegi ' + str(b) + ' jest liczba ' + str(c))

moje_potegowanie(3)
moje_potegowanie(3, b=10)
print()

def moje_dzialanie(dzialanie = 'dodawanie'):
    a = float(input('Podaj wartość a: '))
    b = float(input('Podaj wartość b: '))
    if dzialanie == 'dodawanie':
        c = a + b
    elif dzialanie == 'odejmowanie':
        c = a - b
    elif dzialanie == 'mnożenie':
        c = a * b
    elif dzialanie == 'dzielenie':
        if b == 0:
            print('Nie dziel przez zero!')
        else:
            c = a / b
    else:
        print('Błędna nazwa działania.')
    print(c)

moje_dzialanie()
moje_dzialanie('mnożenie')