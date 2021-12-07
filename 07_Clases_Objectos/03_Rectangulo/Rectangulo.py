class Rectangulo:
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def mostrar_area_calculada(self) -> None:
        print(f'''
            Base: {self.base}
            Altura: {self.altura}
            Area: {self.calcular_area()}
        ''')

base = int(input('Ingrese base: '))
altura = int(input('Ingrese altura: '))

rectangulo1 = Rectangulo(base, altura)
rectangulo1.mostrar_area_calculada()
