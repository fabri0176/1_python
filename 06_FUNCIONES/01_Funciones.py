def suma(a: int = 0, b: int = 0) -> int:
    return a + b

# Función con argumentos variables


def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Nestor', 'Fabricio')


def suma2(*numeros) -> int:
    result = 0
    for numero in numeros:
        result += numero

    return result


resultado_suma = suma2(1+3+4+5+5+6+7)

print(resultado_suma)
