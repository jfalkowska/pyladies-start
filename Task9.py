#Task1
height = float(input('Podaj swój wzrost  w metrach: '))
weight = float(input('Podaj swoją wagę w kilogramach: '))
bmi = weight/height**2
print('Twoje BMI to: ' + str((round(bmi, 2))))
print()

if float(bmi) < 20:
    print ('Masz niedowagę.')
elif float(bmi) > 25:
    print ('Masz nadwagę.')
else:
    print ('Twoja waga jest w normie.')
print()

#Task2
a = float(input('Podaj długość pierwszego boku podstawy (a) w centymetrach: '))
b = float(input('Podaj długość drugiego boku podstawy (b) w centymetrach: '))
c = float(input('Podaj długość wysokości (c) w centymetrach: '))

objetosc_prostopadloscianu = a * b * c
print()

print ('Objętość prostopadłościanu wynosi: ' + str(objetosc_prostopadloscianu) +  ' cm3.')

if a == b:
    print('Podstawa jest kwadratem.')
else:
    print('Podstawa nie jest kwadratem.')

if a == b == c:
    print('Bryła jest sześcianem.')
else:
    print('Bryła nie jest sześcianem.')
print()

# Task2 refactor
a = float(input('Podaj długość pierwszego boku w centymetrach: '))
b = float(input('Podaj długość drugiego boku w centymetrach: '))
c = float(input('Podaj długość trzeciego boku w centymetrach: '))

objetosc_prostopadloscianu = a * b * c
print()

print('Objętość prostopadłościanu wynosi: ' + str(objetosc_prostopadloscianu) + ' cm3.')

if a == b == c:
    print('Bryła jest sześcianem.')
else:
    print('Bryła nie jest sześcianem.')
    if a == b or b == c or a == c:
        print('Ale co najmniej dwie ściany są kwadratami.')
    else:
        print('Żadna ściana nie jest kwadratem.')
