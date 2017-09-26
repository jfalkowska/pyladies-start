mlista = ['pies', 'kot', 'ptaszek']
mlista += ['chomik', 'rybki']
print(mlista)
print()

database = {
    'Marta': {
        'surname': 'Nowak',
        'birth_date': '11/08/1990',
        'profession': 'shopkeeper',
        'interests': [
            'reading'
        ],
        'account_status': 2.00,
    },
    'Tomasz': {
        'surname': 'Kowal',
        'birth_date': '10/09/1987',
        'profession': 'teacher',
        'interests': [
            'swimming'
        ],
        'account_status': 10.00
    }
}

print(database['Marta']['birth_date'])
age_to_edit = database['Marta']['birth_date']
age_to_edit_list = (list(age_to_edit))

year_in_a_list = age_to_edit_list[-4:]
joint_year = int(''.join(year_in_a_list))
new_year = joint_year + 5
print('Twój nowy rok urodzenia to: ' + str(new_year))
