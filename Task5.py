# txt = 'To jest {0} tekst o {1}'.format('fajny', 'mnie')
# print(txt)

name = input('Podaj imię Twojego przyjaciela ').capitalize()
surname = input('Podaj nazwisko Twojego przyjaciela ').capitalize()
title = input('Podaj tytuł naukowy przyjaciela ').capitalize()
adjective = input ('Podaj przymiotnik określający Twojego przyjaciela ').capitalize()
favourite_taste = input ('Podaj ulubiony smak przyjaciela ').lower()

txt = '{0} {1} {2},\n\n{3} przyjacielu chciałbym Cię zaprosić na swoje urodziny, ' \
      'na których będę serwował Twój ulubiony {4} tort. \n\n   Piotr'.format(title, name, surname, adjective, favourite_taste)
print()
print(txt)