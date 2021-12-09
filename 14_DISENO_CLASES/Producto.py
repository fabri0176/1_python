class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio) -> None:

        Producto.contador_productos += 1

        self._id = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    def __str__(self) -> str:
        return f'ID: {self._id}, NOMBRE: {self._nombre}, PRECIO: {self._precio}'


if __name__ == '__main__':
    producto1 = Producto(precio=75, nombre='Camisa')
    producto2 = Producto(precio=150, nombre='Pantalon')

    print(producto1)
    print(producto2)
