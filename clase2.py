 # Flujo de control 

 # Condicionales 


#  a*x + b = 0 

"""a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))
"""

# if condicion:
	# linea de ejecucion	
	# linea de ejecucion
	# linea de ejecucion	
	# linea de ejecucion	
	# linea de ejecucion	
	# linea de ejecucion

# else:
	# linea de ejecucion	
	# linea de ejecucion
	# linea de ejecucion	
	# linea de ejecucion

"""if a==0:
	print("b = "+str(0))

else:
	print("x = "+str(-b/a))
"""

"""
edad = int(input(" Cual es tu edad? "))

if  edad>0:

	if edad>17:
		print("puedes entrar a ver la pelicula ")
	

	else:
		print("No puedes ver la pelicula ")

else:
	print("Tu edad no puede ser menor a cero")
"""



# ------------negativos----------------------0--------------------positivos-------------------

"""
numero = float(input("Introduce un numero: "))

if numero>0:
	print("El numero "+str(numero)+" es positivo")

elif numero<0:
	print("El numero "+str(numero)+" es negativo")

else:
	print("El numero es cero")"""



""" 
if condicion 1 :
	lineas de ejecucion
	lineas de ejecucion
	lineas de ejecucion
	lineas de ejecucion
	lineas de ejecucion

elif condicion2:
	lineas de ejecucion
	lineas de ejecucion
	lineas de ejecucion
	lineas de ejecucion

elif condicion3:
	lineas de ejecucion
	lineas de ejecucion
	lineas de ejecucion

.
.
.

elif condicion N :
	lineas de ejecucion
	lineas de ejecucion
	lineas de ejecucion


else:
	lineas de ejecucion
	lineas de ejecucion
	lineas de ejecucion
	lineas de ejecucion


"""


#  a*x**2 + b*x + c = 0
"""from math import sqrt

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))


if a == 0:
	if b==0:
		print("hay infinitas soluciones")

	else:
		print("la solucion es: "+str(-b/c))

else:
	if b**2 - (4*a*c)>0:

		x1 = (-b +sqrt(b**2 - (4*a*c)))/(2*a)

		x2 = (-b -sqrt(b**2 - (4*a*c)))/(2*a)

		print("la primera solucion es "+str(x1)+" y la segunda solucion es "+str( x2) )

	else:
		print("no existe solucion ")


"""


## diametro 2 veces el radio

# perimetro 2 veces pi por el radio

# el area es pi por el radio al cuadrado
"""
from math import pi

radio = float(input("Ingrese el valor del radio: "))

opcion = (input("Pulse 1) si desea calcular diametro, 2) si desea calcular perimetro y 3) si desea calcular el area "))


if int(opcion) == 1:
	print("el diametro es: ")
	print(2*radio)

elif int(opcion) ==2 :
	print("el perimetro es: ")
	print(2*pi*radio)


elif int(opcion)==3:
	print("el area es: ")
	print(pi*(radio**2))

else:
	print("valor invalido")
	print("Ejecute de nuevo e ingrese un valor entre 1,2 y 3") """



