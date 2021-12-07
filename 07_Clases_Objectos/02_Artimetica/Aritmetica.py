class Aritmetica:
    """ Clase Aritmetica """

    def __init__(self, operandoA, operandoB) -> None:
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self) -> int:
        return self.operandoA + self.operandoB


aritmetica = Aritmetica(5, 4)
print(aritmetica.sumar())
