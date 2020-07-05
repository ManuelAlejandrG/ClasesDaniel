from math import pi

""" Primer ejercicio. Realizar un programa en el que el 
usuario ingrese por pantalla el radio de una circunferencia """

radio_circ = float(input("Ingrese radio de la circunferencia: "))
radio = (pi * 2) * radio_circ
print("El diametro de la circunferencia es: ",radio)



radio_circ = float(input("Ingrese radio de la circunferencia: "))
area = pi * (radio_circ ** 2)
print(" El area de la circunferencia es: ", area)

# Area de un triangulo

base = float ( input (" Ingresa la base del triangulo: ") )
altura = float ( input ( "  Ingrese la altura del triangulo: ") )
area = ( base * altura ) / 2
print("El area del triangulo es: ", area)

#Area y perimetro del cuadrado
base = float(input("Ingrese la base del cuadrado: "))
altura = float(input("Ingrese la altura del cuadrado: "))
area = (base) * (altura)
print("El area del cuadrado es: ", int(area))

#Perimetro de un cuadrado

base = float(input("Ingrese la base del cuadrado: "))
altura = float(input("Ingrese la altura del cuadrado: "))
perimetro = (base + base) + (altura + altura)
print("El area del cuadrado es: ", int(perimetro))

#Ejercicio volumen

radio = float(input("Ingrese la medida del radio : "))
volum = 4/3 * pi
print(volum)