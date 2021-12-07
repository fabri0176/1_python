class Persona:

    def __init__(self, nombres, apellidos, edad) -> None:
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad

    def mostrar_detalle(self) -> None:
        print(f'''
        Nombres: {self.nombres}
        Apellidos: {self.apellidos}
        Edad: {self.edad}
        
        ''')

    def __str__(self) -> str:
        pass


persona1 = Persona("Néstor Fabricio", "Parra", 30)
persona1.mostrar_detalle()
