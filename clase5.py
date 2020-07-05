## CLASES EN PYTHON

## ORIENTADO OBJETOS


"""class Animal:
    color = "Negro"
    patas = 4

    def camina(self):
        return "está caminando"


perro = Animal()

print(type(perro))
"""

"""
class Vehiculo:
    gasolina = 0
    ruedas = 4

    def avanzar(self):
        if self.gasolina != 0:
            self.gasolina -= 1
            return "El carro avanza y tiene {} de gasolina".format(self.gasolina)

        else:
            return "El vehiculo no tiene gasolina"

    def recargar(self, recarga=1):
        self.gasolina += recarga
        return "Tiene {} de gasolina".format(self.gasolina)


forfi = Vehiculo()

print(forfi.avanzar())

print(forfi.recargar())

print(forfi.avanzar())
"""


class Vehiculo:
    """ La cjfsapjfpsfjpas """
    def __init__(self, numero_de_ruedas: int, marca: str, c: str, gasolina=1):
        """metodo inicuasasojf"""
        self.ruedas = numero_de_ruedas
        self.marca = marca
        self.color = c
        self.gasolina = gasolina

    def __str__(self):
        return "El Vehiculo tiene {} ruedas, la marca es {} y el color es {}".format(self.ruedas, self.marca, self.color)

    def avanzar(self):
        if self.gasolina != 0:
            self.gasolina -= 1
            print("El vehiculo avanza y tiene {} de gasolina".format(self.gasolina))

        else:
            print("El vehiculo no tiene gasolina")

    def recargar(self, recarga=1):
        self.gasolina += recarga
        print( "Tiene {} de gasolina".format(self.gasolina))





"""
ferrari = Vehiculo(4,"ferrari","rojo")

ferrari.recargar(20)

print(ferrari)
moto = Vehiculo(2, "Ducatti", "Negra")

moto.avanzar()
"""


# HERENCIA Y POLIMORFISMO

