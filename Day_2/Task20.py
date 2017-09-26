print()
def objetosc_prostopadloscianu(a, b, h):
    c = a * b * h
    print('Objętność prostopadłościanu wynosi: ' + str(c) + ' cm3.')

objetosc_prostopadloscianu(2, 2, 7)

print()
def bmi (weight, height):
    bmi = weight / height ** 2
    print('Twoje BMI to: ' + str((round(bmi, 1))))

bmi(55, 1.6)