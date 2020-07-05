from agenda import Agenda
from clase5 import Vehiculo

Manuel = Agenda("Manuel", "+584125196037")

Manuel.agregar_contacto("Juan", "+584145551014")

print(Manuel)


moto = Vehiculo(2,"Yamaha", "roja")

moto.recargar(20)
print(moto)