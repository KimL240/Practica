#Implementar una clase `Círculo` con atributo `radio` y un método que calcule el área.
import math

class Circulo:
     def __init__(self,radio):
         self.radio=radio
     def calculara_area(self):
         area=math.pi * (self.radio)
         print(f'El area del circulo con radio {self.radio} es: {area:.2f}')

Circulo1=Circulo(5)
Circulo1.calculara_area()