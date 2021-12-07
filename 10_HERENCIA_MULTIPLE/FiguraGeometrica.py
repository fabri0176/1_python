class FiguraGeometrica:

    def __init__(self, ancho, alto) -> None:
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto
