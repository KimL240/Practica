#Crear una clase `Usuario` con nombre completo generado mediante `@property`.
class Usuario:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad > 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un número entero positivo.")

    @property
    def es_adulto(self):
        return self._edad >= 18

usuario = Usuario("Carlos", 22)
print(f"Nombre: {usuario.nombre}, Edad: {usuario.edad}, ¿Es adulto? {usuario.es_adulto}")

usuario.edad = 15
print(f"Edad actualizada: {usuario.edad}, ¿Es adulto? {usuario.es_adulto}")
