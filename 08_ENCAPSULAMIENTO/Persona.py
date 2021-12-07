class Persona:
    def __init__(self, nombres, apellidos, num_identificacion) -> None:
        self._nombres = nombres
        self._apellidos = apellidos
        self._num_identificacion = num_identificacion

    @property
    def nombres(self):
        return self._nombres

    @property
    def apellidos(self):
        return self._apellidos

    @property
    def num_identificacion(self):
        return self._num_identificacion

    @nombres.setter
    def nombres(self, nombres):
        self._nombres = nombres

    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    @num_identificacion.setter
    def num_identificacion(self, num_identificacion):
        self._num_identificacion = num_identificacion


persona1 = Persona('Nestor Fabricio', 'Parra Gonzalez', 123213123)

print(f'Soy {persona1.nombres} {persona1.apellidos} CC {persona1.num_identificacion}')

persona1.num_identificacion = 21313123213

print(f'Soy {persona1.nombres} {persona1.apellidos} CC {persona1.num_identificacion}')