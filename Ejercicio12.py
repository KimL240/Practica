#Crear una clase `Temperatura` con `@property` para convertir de Celsius a Fahrenheit.
class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        self._celsius = valor

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperatura(25)
print(f"{temp.celsius}°C es igual a {temp.fahrenheit}°F")

temp.celsius = 30
print(f"{temp.celsius}°C es igual a {temp.fahrenheit}°F")
