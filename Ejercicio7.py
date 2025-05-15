#Crear una clase `Libro` con métodos para mostrar título y autor.
class Libro:
    def __init__(self,titulo, autor, año):
        self.titulo=titulo
        self.auto=autor
        self.año=año
    def mostrar_informacion(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.auto}')
        print(f'Año de publicacion: {self.año}')
        
Libro1=Libro('El Señor de los Anillos. Edición ilustrada por el autor','J.R.R.Tolkien',1954)
Libro1.mostrar_informacion()
