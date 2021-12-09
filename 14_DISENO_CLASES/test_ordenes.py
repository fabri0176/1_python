from Orden import Orden
from Producto import Producto

producto1 = Producto(precio=75, nombre='Camisa')
producto2 = Producto(precio=150, nombre='Pantalon')

productos = [producto1, producto2]

orden1 = Orden(productos)

orden1.add_producto(Producto('Zapatos', 200))


print(orden1.calcular_total())
