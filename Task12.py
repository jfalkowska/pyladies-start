shopping_list = [
    [input('Podaj pierwszy produkt żony: '), input('Podaj drugi produkt żony: '), input('Podaj trzeci produkt żony: ')],
    [input('Podaj pierwszy produkt męża: '), input('Podaj drugi produkt męża: '), input('Podaj trzeci produkt męża: ')]
]
print()

wife_request_bought = []
wife_request_not_bought = []
excess_shopping = []

if shopping_list[0][0] == shopping_list[1][0] or shopping_list[0][0] == shopping_list[1][1] or shopping_list[0][0] == shopping_list[1][2]:
    wife_request_bought.append(shopping_list[0][0])
else:
    wife_request_not_bought.append(shopping_list[0][0])

if shopping_list[0][1] == shopping_list[1][0] or shopping_list[0][1] == shopping_list[1][1] or shopping_list[0][1] == shopping_list[1][2]:
    wife_request_bought.append(shopping_list[0][1])
else:
    wife_request_not_bought.append(shopping_list[0][1])

if shopping_list[0][2] == shopping_list[1][0] or shopping_list[0][2] == shopping_list[1][1] or shopping_list[0][2] == shopping_list[1][2]:
    wife_request_bought.append(shopping_list[0][2])
else:
    wife_request_not_bought.append(shopping_list[0][2])

if shopping_list[1][0] != shopping_list[0][0] and shopping_list[1][0] != shopping_list[0][1] and shopping_list[1][0] != shopping_list[0][1]:
    excess_shopping.append(shopping_list[1][0])

if shopping_list[1][1] != shopping_list[0][0] and shopping_list[1][1] != shopping_list[0][1] and shopping_list[1][1] != shopping_list[0][1]:
    excess_shopping.append(shopping_list[1][1])

if shopping_list[1][2] != shopping_list[0][0] and shopping_list[1][2] != shopping_list[0][1] and shopping_list[1][2] != shopping_list[0][2]:
    excess_shopping.append(shopping_list[1][2])

print('Wife request bought: ',end='')
for item in wife_request_bought:
    print(item,end='; ')
print()

print('Wife request not bought: ',end='')
for item in wife_request_not_bought:
    print(item,end='; ')
print()

print('Excess shopping: ',end='')
for item in excess_shopping:
    print(item,end='; ')