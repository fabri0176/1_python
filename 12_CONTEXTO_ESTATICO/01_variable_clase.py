class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia) -> None:
        self._variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico(datos) -> None:
        print(datos, MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)


if __name__ == '__main__':
    MiClase.metodo_estatico('Mensaje para datos')

    MiClase.metodo_clase()
