from Vehiculo import Vehiculo


class Coche(Vehiculo):
    def __init__(self, num_ruedas = 4) -> None:
        super().__init__(num_ruedas)
