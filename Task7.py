#liczy jak tablica, od zera
x = 'text'
print (x[1:])
print (x[:3])
print (x[1:2])
print()

text_1 = 'Ala ma kota a kot ma Alę.'
text_1_length = len(text_1)
text_1_length_divided_by_half = int(text_1_length)/2
print (text_1[:int(text_1_length_divided_by_half)])
print()

text_2 = 'PyLadies.start() ma przerwę obiadową o 14:00'
text_2_length = len(text_2)
text_2_length_divided_by_half = int(text_2_length)/2
print (text_2[:int(text_2_length_divided_by_half)])
