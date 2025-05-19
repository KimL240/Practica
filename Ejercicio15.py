class Carro:
    def __init__(self):
        self.motor_encendido= False
    def encender(self):
        if not self.motor_encendido:
            self.motor_encendido= True
            print('Motor Encendido')
        else:
            print('El motor ya estaba encendido')
            
    def apagar(self):
        if self.motor_encendido:
            self.motor_encendido= False
            print('Motor apagado')
        else:
            print('El motor ya estaba apagado')
    def mostrar_estado(self):
        estado = 'Encendido' if self.motor_encendido else 'Apagado'
        print(f'El motor esta {estado}')
   
mi_carro=Carro()
mi_carro.encender()
mi_carro.mostrar_estado()
mi_carro.apagar()
mi_carro.mostrar_estado()      
    