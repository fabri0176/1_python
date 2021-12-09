from Producto import Producto


class Orden:

    contador_ordenes = 0

    def __init__(self, productos) -> None:
        Orden.contador_ordenes += 1

        self._id = Orden.contador_ordenes
        self._productos = list(productos)

    def add_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio

        return total

    def __str__(self) -> str:
        productos_str = ''

        for producto in self._productos:
            productos_str += producto.__str__()+'|'

        return f'Orden: {self._id}, \nProductos: {productos_str}'


if __name__ == '__main__':
    producto1 = Producto(precio=75, nombre='Camisa')
    producto2 = Producto(precio=150, nombre='Pantalon')

    productos = [producto1, producto2]

    orden1 = Orden(productos)

    print(orden1)
