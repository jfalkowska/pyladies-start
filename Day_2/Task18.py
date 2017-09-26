print()
print('Policz swoje BMI!')
print()
height = float(input('Podaj swój wzrost  w metrach: '))
weight = float(input('Podaj swoją wagę w kilogramach: '))
bmi = weight/height**2
print('Twoje BMI to: ' + str(bmi))
print()

finish = False
while not finish:
    answer = input('Czy chcesz policzyć kolejne BMI? ')
    if answer == 'tak':
        height = float(input('Podaj swój wzrost  w metrach: '))
        weight = float(input('Podaj swoją wagę w kilogramach: '))
        bmi = weight / height ** 2
        print('Twoje BMI to: ' + str(bmi))
        print()
    else:
        finish = True
        print('Do zobaczenia!')
print()
