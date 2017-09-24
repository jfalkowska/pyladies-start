print('1a. Policz swoje BMI')
height = float(input('Podaj swój wzrost  w metrach '))
weight = float(input('Podaj swoją wagę w kilogramach '))
print('Twoje BMI to: ' + str(weight/height**2))
print()

print('1b. Policz swoje BMI ładniejszym kodem')
height = float(input('Podaj swój wzrost  w metrach '))
weight = float(input('Podaj swoją wagę w kilogramach '))
bmi = weight/height**2
print('Twoje BMI to: ' + str(bmi))
print()

print('2a. Policz pole prostokąta')
a = float(input('Podaj długość pierwszego boku w centymetrach ' ))
b = float(input('Podaj długość drugiego boku w centymatrach ' ))
print('Pole Twojego prostokąta wynosi ' + str(a*b) + ' cm2')
print()

print('2b. Policz pole prostokąta ładniejszym kodem')
a = float(input('Podaj długość pierwszego boku w centymetrach ' ))
b = float(input('Podaj długość drugiego boku w centymatrach ' ))
area = a*b
print('Pole Twojego prostokąta wynosi ' + str(area) + ' cm2')