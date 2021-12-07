class Aritmetica:
    """ Clase Aritmetica """

    def __init__(self, operandoA, operandoB) -> None:
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self) -> int:
        return self.operandoA + self.operandoB

    def restar(self) -> int:
        return self.operandoA - self.operandoB

    def dividir(self) -> float:
        return self.operandoA / self.operandoB

    def mostrarSuma(self) -> None:
        print(f'La suma es {self.sumar()}')

    def mostrarResta(self) -> None:
        print(f'La resta es {self.restar()}')

    def mostrarDivision(self) -> None:
        print(f'El resultado de la división es {self.dividir():.2f}')


aritmetica = Aritmetica(5, 4)
aritmetica.mostrarResta()
aritmetica.mostrarSuma()
aritmetica.mostrarDivision()


print(aritmetica.restar())
