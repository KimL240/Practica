#Crear una clase `Estudiante` que herede de `Persona` y tenga un atributo `grado`.
class Estudiante:
    def __init__(self,nombre,edad,promedio):
        self.nombre=nombre
        self.edad=edad
        self.promedio=promedio
    def esta_aprobado(self):
        if self.promedio >= 60:
            print(f'{self.nombre} esta aprobado con un promedio de {self.promedio}')
        else:
            print(f'{self.nombre} no esta aprobado con un buen promedio {self.promedio}')
            
Estudiante1=Estudiante('Lis velas', 50,90)
Estudiante2=Estudiante('Kim Ben',20,50)

Estudiante1.esta_aprobado()
Estudiante2.esta_aprobado()