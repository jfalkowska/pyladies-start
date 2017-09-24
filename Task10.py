name1 = input('Podaj imię pierwszej osoby: ')
age1 = input('Podaj wiek pierwszej osoby: ')
name2 = input('Podaj imię drugiej osoby: ')
age2 = input('Podaj wiem drugiej osoby: ')
name3 = input('Podaj imię trzeciej osoby: ')
age3 = input('Podaj wiek trzeciej osoby: ')
print()

list1 = [name1,age1]
list2 = [name2, age2]
list3 = [name3, age3]
list_of_lists = [list1, list2, list3]

print ('Person one: ' + list_of_lists[0][0] + ', ' + list_of_lists[0][1])
print ('Person two: ' + list_of_lists[1][0] + ', ' + list_of_lists[1][1])
print ('Person three: ' + list_of_lists[2][0] + ', ' + list_of_lists[2][1])
print()

print ('List of lists: ' + list_of_lists[0][0] + ', ' + list_of_lists[0][1] + ', '+ list_of_lists[1][0] + ', ' + list_of_lists[1][1] + ', ' + list_of_lists[2][0] + ', ' + list_of_lists[2][1])
print()

print('List of names: ' + list_of_lists[0][0] + ', ' + list_of_lists[1][0] + ', ' + list_of_lists[2][0])
print('List of ages: ' + list_of_lists[0][1] + ', ' + list_of_lists[1][1] + ', ' + list_of_lists[2][1])

