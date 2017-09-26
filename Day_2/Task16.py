for number in range(0,11):
    print(number)

from pprint import pprint as pp

zliczacz = {}
wyraz = input('Podaj wyraz: ')
for let in wyraz:
    if let in zliczacz:
        zliczacz[let] += 1
    else:
        zliczacz[let] = 1
pp(zliczacz)