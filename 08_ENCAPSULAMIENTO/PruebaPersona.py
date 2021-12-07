from Persona import Persona

print('Creación objetos'.center(50, '-'))

persona1 = Persona('Katherine Lisset', 'Ortega R.', 112123123)
persona1.mostrar_detalle()

print('Eliminación objetos'.center(50, '-'))
del persona1
