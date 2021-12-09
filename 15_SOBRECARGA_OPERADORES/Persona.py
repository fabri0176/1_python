class Persona:
    def __init__(self, nombre) -> None:
        self._nombre = nombre

    def __add__(self, other):
       return f'{self.nombre} +  {other.nombre}'

    @property
    def nombre(self):
        return self._nombre


persona1 = Persona('Nestor')
persona2 = Persona('Fabricio')

print(persona1 + persona2)