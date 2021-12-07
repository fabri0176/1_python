from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, lado, color) -> None:
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
