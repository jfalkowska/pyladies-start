# print()
# def is_it_a_number(text):
#     if isinstance(text, (int, float)):
#         return text
#     if not isinstance(text, str):
#         return False
#     text = text.replace(',', '.')
#     try:
#         float(text)
#         return text
#     except ValueError:
#         return 'Wprowadź poprawne wartości.'
#
# print (is_it_a_number('3,3'))
# print()

def height_function():
    while True:
        height = input('Podaj swój wzrost  w metrach: ')
        try:
            return float(height)
        except ValueError:
            print('Wprowadź poprawne wartości.')

def weight_function():
    weight = input('Podaj swoją wagę w kilogramach: ')
    if isinstance(weight, (int, float)):
        return weight
    if not isinstance(weight, str):
        return False
    weight = weight.replace(',', '.')
    try:
        float(weight)
        return weight
    except ValueError:
        return 'Wprowadź poprawne wartości.'

x = height_function()
y = weight_function()

# bmi = weight/height**2
bmi = y/x**2

print('Twoje BMI to: ' + str((round(bmi, 2))))
print()

if float(bmi) < 20:
    print ('Masz niedowagę.')
elif float(bmi) > 25:
    print ('Masz nadwagę.')
else:
    print ('Twoja waga jest w normie.')
print()