#Crear una clase `Vehiculo` con atributos comunes y luego clases hijas como `Carro` y
#`Moto` que hereden de ella.
class auto:
    def __init__(self, marca, modelo, año):
        self.marca=marca
        self.modelo=modelo
        self.año=año
    def descripcion_completa(self):
        print(f'La marca del auto es: {self.marca}, y este es un modelo {self.modelo}, del año {self.año}')
        
mi_auto=auto('Toyota','corolla', 2022)
mi_auto.descripcion_completa()
     