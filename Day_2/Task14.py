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

account_status = float(database['Marta']['account_status'])
double_account_status = account_status*2
database['Marta']['account_status'] = double_account_status
print(database['Marta']['account_status'])

database['Tomasz']['interests'].append('climbing')
database['Tomasz']['interests'].append('snorkelling')
print(database['Tomasz']['interests'])

database['Tomasz']['surname'] = 'Kowal-Mąż'
print(database['Tomasz']['surname'])

database['Marta']['middle_name'] = 'Maria'
print(database['Marta']['middle_name'])
database['Tomasz']['middle_name'] = ''
print(database['Tomasz']['middle_name'])

database['Marta']['age'] = '30'
print(database['Marta']['age'])
database['Tomasz']['age'] = '35'
print(database['Tomasz']['age'])

database['Marta']['education'] = 'M.A.'
print(database['Marta']['education'])
database['Tomasz']['education'] = 'B.A.'
print(database['Tomasz']['education'])

del database['Marta']['birth_date']
print(database['Marta'])
del database['Tomasz']['birth_date']
print(database['Tomasz'])