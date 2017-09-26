# TO DO:
# add if isinstance and change str 0,0 to float 0.0

def height_function():
    while True:
        height = input('Podaj swój wzrost  w metrach: ')
        try:
            return float(height)
        except ValueError:
            print('Wprowadź poprawne wartości.')

def weight_function():
    while True:
        weight = input('Podaj swoją wagę w kilogramach: ')
        try:
            return float(weight)
        except ValueError:
            print('Wprowadź poprawne wartości.')

def calculate_bmi():
    bmi = y / x ** 2

    print('Twoje BMI to: ' + str((round(bmi, 2))))
    print()

    if float(bmi) < 20:
        print('Masz niedowagę.')
    elif float(bmi) > 25:
        print('Masz nadwagę.')
    else:
        print('Twoja waga jest w normie.')
    print()

x = height_function()
y = weight_function()
calculate_bmi()

