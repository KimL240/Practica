#Crear una clase `Empleado` con método `calcular_salario()` y sobrescribirlo en
#`EmpleadoTiempoCompleto` y `EmpleadoPorHora`.
class Empleado:
    def __init__(self, nombre):
        self.nombre=nombre
    def calcular_salario(self):
        print('Este metodo debe ser implementado por las subclases')
    
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre,salario_mensual):
        super().__init__(nombre)
        self.salario_mensual=salario_mensual
    def calcular_salario(self):
        print(f'{self.nombre} (Tiempo_completo): Salario mensual $ {self.salario_mensual:,.2f}')
        
class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, horas_trabajadas, taraifa_hora):
        super().__init__(nombre)
        self.horas_trabajadas=horas_trabajadas
        self.tarifa_hora=taraifa_hora
    def calcular_salario(self):
        salario=self.horas_trabajadas * self.tarifa_hora
        print(f'{self.nombre} (Por Hora): Salario por {self.horas_trabajadas} horas=${salario:,.2f}')

empleado1=EmpleadoTiempoCompleto('Josue martinez', 5000.00)
empleado2=EmpleadoPorHora('Daniela Gonzales',120,18.75)

empleados=[empleado1, empleado2]

for emp in empleados:
    emp.calcular_salario()    
