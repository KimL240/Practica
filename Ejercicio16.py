from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

rect = Rectangulo(5, 3)
print(f"Área del rectángulo: {rect.area()}")