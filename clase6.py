

class Vehiculo:

    def __init__(self, color, marca, gasolina=1):
        self.color = color
        self.marca = marca
        self.gasolina = gasolina

    def andar(self):
        return "El vehiculo esta andando"

    def recargar(self, n=1):
        self.gasolina += n
        return "El vehiculo tiene {} de gasolina".format(n)

    def __str__(self):
        return "marca {} de color {}".format(self.marca, self.color)


class Moto(Vehiculo):

    def __init__(self, color, marca, ruedas, gasolina, paquete):
        Vehiculo.__init__(self, color, marca, gasolina)
        self.paquete = paquete
        self.ruedas = ruedas

    def caballito(self):
        return "La moto esta haciendo caballito"

    def __str__(self):
        return "La moto es " + Vehiculo.__str__(self) + " tiene {} ruedas".format(self.ruedas)


class Autobus(Vehiculo):

    def __init__(self, color, marca, ruedas, gasolina, pasajeros):
        super().__init__(color, marca, gasolina)
        self.pasajeros = pasajeros
        self.ruedas = ruedas

    def __str__(self):
        return "El autobus es " + super().__str__() + " tiene {} ruedas y lleva {} pasajeros".format(self.ruedas,
                                                                                                     self.pasajeros)


bus = Autobus(color="amarillo", marca="volvo", ruedas='6', gasolina=10, pasajeros=35)
print(bus)
print(bus.andar())
