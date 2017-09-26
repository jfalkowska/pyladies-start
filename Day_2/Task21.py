print()
def objetosc_prostopadloscianu(a, b, h):
    c = a * b * h
    return c

x = objetosc_prostopadloscianu(2, 2, 7)
print(x)

print()
def bmi (weight, height):
    bmi = weight / height ** 2
    return float(round(bmi, 1))

z = bmi(55, 1.6)
print(z)
