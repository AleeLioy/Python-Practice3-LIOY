class Vehiculo:
    def __init__(self, patente, descripcion=""):
        self.patente = patente
        self.descripcion = descripcion

    def mostrar(self):
        print("Patente:", self.patente)
        print("Descripción:", self.descripcion)

    def validarPatente(self):
        if (len(self.patente) == 6 or len(self.patente) == 8):
            return True
        return False

Auto1 = Vehiculo("AA345BB", "AutoPRO")
#Auto1.mostrar()
#print(Auto1.validarPatente())

class Estadia:
    def __init__(self, vehiculo, hora_entrada, hora_salida):
        self.vehiculo = vehiculo
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida

    def mostrar(self):
        self.vehiculo.mostrar()
        print("Hora de entrada:", self.hora_entrada)
        print("Hora de salida:", self.hora_salida)

    def calcularTarifaTotal(self, tarifaPorHora):
        if (self.vehiculo.validarPatente()==True):
            if (self.hora_entrada > self.hora_salida):
                return (self.hora_salida*self.hora_entrada)*tarifaPorHora

estadia=Estadia(Auto1, 6, 10)
estadia.mostrar()
print(estadia.calcularTarifaTotal)