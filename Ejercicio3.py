#Crear una clase `CuentaBancaria` con métodos para depositar y retirar dinero.
class cuentaBancaria:
    def __init__(self,titular,saldo):
        
        self.titular=titular
        self.saldo=saldo
        
    def depositar(self,monto):
        if monto > 0:
            self.saldo+=monto 
            print(f'Depositaste ${monto}.saldo actual $ {self.saldo}')
        else:
            print('Monto Invalido.')
            
    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            print(f'Retiraste $ {monto}. saldo restante: $ {self.saldo}')
        else:
            print(f'Fondos insuficientes o monto invalido.')
    def consultar_saldo(self): 
        print(f'{self.titular}, tu saldo es: $ {self.saldo}')
        

cuenta1=cuentaBancaria('Jose Martinez',5000)
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.consultar_saldo()