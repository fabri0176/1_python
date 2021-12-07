from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):

    def __init__(self, num_ruedas = 2) -> None:
        super().__init__(num_ruedas)


if __name__ == '__main__':
    bicicleta = Bicicleta(3)
    
    