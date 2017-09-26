print()

dictionary = {
    'cd': 'si-di',
    'dvd': 'di-wi-di',
}
words_to_process = []

word = input('Podaj wyszukiwane słowo: ').lower()

if word in dictionary:
    print('Wymowa Twojego słowa to: ' + dictionary[word])
else:
    print('Nie mamy takiego słowa w bazie danych. Wkrótce uzupełnimy słownik.')
    dictionary[word] = ''
    words_to_process.append(word)
print()

answer = input('Czy chcesz uzupełnić bazę danych? ').lower()
if answer == 'tak':
    print('Super!')
    print('Lista słów do uzupełnienia: ' + str(words_to_process))
else:
    print('Nie to nie.')
