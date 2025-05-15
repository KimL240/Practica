#Implementar una clase `Rectángulo` con métodos para calcular el perímetro y el área.
class Rectangulo:
    def __init__(self,base, altura):
        self.base=base
        self.altura=altura
    def calcular_area(self):
        print(f'El area del rectangulo es: {self.base * self.altura}')
    def calcular_perimetro(self):
        print(f'El perimetro del rectangulo es: {2 * self.base * self.altura}')

rectangulo1=Rectangulo(8,5)
rectangulo1.calcular_area()
rectangulo1.calcular_perimetro()
        