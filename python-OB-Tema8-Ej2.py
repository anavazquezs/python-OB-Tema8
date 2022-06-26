import pickle


class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    
    def getMarca(self):
        return self.marca

miAuto1 = Vehiculo('Fiat', '2020', 10000)

# f = open('datosVehiculo.bin', "x")

# f = open('datosVehiculo.bin', 'wb')

# pickle.dump(miAuto1, f)

# f.close()

f = open('datosVehiculo.bin', 'rb')

miAuto1 = pickle.load(f)
f.close()

print(type(miAuto1))

print(miAuto1.getMarca())
