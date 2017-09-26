database = {
    'Marta': {
        'surname': 'Nowak',
        'birth_date': '11/08/1990',
        'profession': 'shopkeeper',
        'interests': 'reading',
        'account_status': '0.00 PLN',
    },
    'Tomasz': {
        'surname': 'Kowal',
        'birth_date': '10/09/1987',
        'profession': 'teacher',
        'interests': 'swimming',
        'account_status': '10.00 EUR'
    }
}

print(database['Marta'])
print(database['Tomasz']['interests'])
print(database['Marta'], database['Tomasz']['interests'])
