#Implementar `@property` en una clase `Rectángulo` para calcular el área
#automáticamente.

class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor > 0:
            self._ancho = valor
        else:
            raise ValueError("El ancho debe ser mayor a cero.")

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor > 0:
            self._alto = valor
        else:
            raise ValueError("El alto debe ser mayor a cero.")

    @property
    def area(self):
        return self._ancho * self._alto

rect = Rectangulo(5, 10)
print(f"Ancho: {rect.ancho}, Alto: {rect.alto}, Área: {rect.area}")

rect.ancho = 8
print(f"Nuevo ancho: {rect.ancho}, Área actualizada: {rect.area}")
