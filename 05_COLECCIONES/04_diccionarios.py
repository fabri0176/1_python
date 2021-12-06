diccionario = {
    'IDE': 'Integrated development enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Mangement '
}


print(diccionario['IDE'])

print(diccionario.get('OOP'))

for index, value in diccionario.items():
    print(f'{index}: {value}')

# VALIDAR EXISTENCIA DE UN ELEMENTO DICCIONARIO
print('IDE' in diccionario)


diccionario.pop('DBMS')
