#Implementar encapsulamiento en una clase `Producto`, ocultando su precio real con
#doble guion bajo (`__precio`).
class producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.__precio=precio
        
    def get_precio(self):
        return self.__precio
    
    def set_precio(self,new_precio):
        self.__precio=new_precio

producto1=producto('jabon',25)

print(producto1.get_precio())
producto1.set_precio(30)
print(producto1.get_precio())
print(producto1.get_precio())