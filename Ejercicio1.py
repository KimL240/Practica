#Crear una clase `Persona` con atributos `nombre` y `edad`, y un método que imprima su
#información.
class Persona:
    
    def __init__(self,nombre,edad):
        
        self.nombre=nombre
        self.edad=edad
        
    def presentar(self):
        print(f'Bienvenido {self.nombre} Espero que la pases bien')
    def presentar_edad(self):
        print(f'La edad de {self.nombre}, Es de {self.edad}')

persona1=Persona('Fernando Martinez', '30')
persona1=Persona('Fernando Martinez','30 años')
persona1.presentar()
persona1.presentar_edad()