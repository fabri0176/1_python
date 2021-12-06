mes = int(input("Ingrese número de mes (1-12)"))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes >= 3 and mes < 6:
    estacion = 'Primavera'
elif mes >= 6 and mes < 9:
    estacion = 'Verano'
else:
    estacion = 'Otoño'

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif 3 <= mes < 6:
    estacion = 'Primavera'
elif 6 <= mes < 9:
    estacion = 'Verano'
else:
    estacion = 'Otoño'

print(f'Para el mes ({mes}) la estación es: {estacion}')
