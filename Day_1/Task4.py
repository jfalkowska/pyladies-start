import math

r = float(input('Podaj promień podstawy w centymetrach '))
l = float(input('Podaj tworzącą stożka w centymetrach '))
h = float(input('Podaj wysokość stożka w centymatrach '))

pole_podstawy = math.pi * r ** 2
pole_powierzchni_bocznej = math.pi * r * l
objetosc = 1/3 * math.pi * r ** 2 * h

print()
print('Pole podstawy stożka wynosi ' + str(pole_podstawy))
print('Pole powierzchni bocznej bocznej wynosi ' + str(pole_powierzchni_bocznej))
print('Objętość stożka wynosi ' + str(objetosc))
