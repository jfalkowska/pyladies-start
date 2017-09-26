#Task1 round
height = float(input('Podaj swój wzrost  w metrach: '))
weight = float(input('Podaj swoją wagę w kilogramach: '))
bmi = weight/height**2
print('Twoje BMI to: ' + str((round(bmi, 2))))
print()

#Task2 round
a = float(input('Podaj wartość boku a: '))
b = float(input('Podaj wartość boku b: '))
c = float((a ** 2 + b**2 )**0.5)
print ('Wartość boku c wynosi: ' + str(round(c, 2)) + '.')