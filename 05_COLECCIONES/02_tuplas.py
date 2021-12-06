# Tipo inmutable
frutas = ('Naranja', 'Platano', 'Limon')

print(frutas)

for fruta in frutas:
    print(fruta, end=', ')


frutasList = list(frutas)
frutasList[0] = 'Pera'

frutas = tuple(frutasList)

print('\n', frutas)

print('----------------------------------------------------------')

numeros = (13, 1, 8, 3, 2, 5, 8)
numerosList = list()
for numero in numeros:
    if numero < 5:
        numerosList.append(numero)


print(numerosList)
