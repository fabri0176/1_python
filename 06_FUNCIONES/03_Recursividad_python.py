def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)


resultado = factorial(5)
print(resultado)


def imprimirNumeros(numero):
    
    print(numero)
    if numero == 1:
        return
    
    imprimirNumeros(numero - 1)    
        

imprimirNumeros(5)
