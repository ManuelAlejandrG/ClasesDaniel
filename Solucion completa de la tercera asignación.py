#1º Ejercicio
# BUENO
num  = int(input("Introduce tú numero: "))
lista_pares = []
lista_impar = []
for i in range (2,num+1):
	if i%2 == 0:
		lista_pares.append(i)
		
		 

	else:
		print("Seria un numero impar")
			

print(lista_pares)

#---------------------------------------------
#2º Ejercicio
# MALO
n  = int(input("Introduce tú numero: "))
m  = int(input("Introduce tú numero: "))

lista_n = []
lista_m = []

for i in range (n+1):
	if i % 2 == 0:
		lista_n.append(i)
	else:
		i & 3 == 0

for i in range (m+1):
	if i % 2 == 0:
		lista_m.append(i)
	else:
		i % 3 == 0
		

print(lista_n)
print(lista_m)
s = sum (lista_n) + sum(lista_m)
print(" El sumatorio es: " + str(s))


#--------------------------------------------
# 3º Ejercicio
# BUENO
while True:
	n  = int(input("Introduce tú numero: "))
	if n > 0:
		print(n)
	else:
		print(" Debe de introducir un numero positivo. Gracias")
		exit()
#-----------------------------------------------------------------------
#4º Ejercicio
""" Quizás muy descabellada la solución, pero después de sopesar varias
soluciones, está me funcionó"""
# BUENO
p  = str(input("Introduce tu palabra con maysculas: "))
l = list(p)
cont = 0
minu = 0
for i in l:
	if i == "H":
		cont = cont+1
	elif i == "Z":
		cont = cont + 1
	elif i == "X":
		cont = cont + 1
	elif i == "C":
		cont = cont + 1
	elif i == "V":
		cont = cont + 1
	elif i == "B":
		cont = cont + 1
	elif i == "N":
		cont = cont + 1
	elif i == "M":
		cont = cont + 1
	elif i == "A":
		cont = cont + 1
	elif i == "S":
		cont = cont + 1
	elif i == "D":
		cont = cont + 1
	elif i == "F":
		cont = cont + 1
	elif i == "G":
		cont = cont + 1
	elif i == "J":
		cont = cont + 1
	elif i == "K":
		cont = cont + 1
	elif i == "L":
		cont = cont + 1
	elif i == "Q":
		cont = cont + 1
	elif i == "W":
		cont = cont + 1
	elif i == "E":
		cont = cont + 1
	elif i == "R":
		cont = cont + 1
	elif i == "T":
		cont = cont + 1
	elif i == "Y":
		cont = cont + 1
	elif i == "U":
		cont = cont + 1
	elif i == "I":
		cont = cont + 1
	elif i == "O":
		cont = cont + 1
	elif i == "P":
		cont = cont + 1
		
	else:
		minu = minu + 1


print(" El numero de mayusculas es: " + str(cont))
#-----------------------------------------------------
#5º Ejercicio
# MALO
d =input(" Ingrese su digito: ")
lista_Uno = list(d)
cont_Digitos = 0
contar_Letras = 0

for i in lista_Uno:
	if i == "1":
		cont_Digitos = cont_Digitos + 1
	elif i == "2":
		cont_Digitos = cont_Digitos + 1
	elif i == "3":
		cont_Digitos = cont_Digitos + 1
	elif i == "4":
		cont_Digitos = cont_Digitos + 1
	elif i == "5":
		cont_Digitos = cont_Digitos + 1
	elif i == "6":
		cont_Digitos = cont_Digitos + 1
	elif i == "7":
		cont_Digitos = cont_Digitos + 1
	elif i == "8":
		cont_Digitos = cont_Digitos + 1
	elif i == "9":
		cont_Digitos = cont_Digitos + 1
	elif i == "0":
		cont_Digitos = cont_Digitos + 1
	else:
		contar_Letras = contar_Letras + 1

if cont_Digitos > 0:
	print("Contiene digitos")
else:
	print("No contiene digitos")

#------------------------------------------------
#6º Ejercicio
# MALO
d =str(input(" Ingrese su palabra y conozca si es alfanumerica: "))
palabra = len(d)
i =0
salida = True

while i + 1 > len(d):
	if d [i] > s[i+1]:
		salida = True

	else:
		salida = False


if salida is True:
	print("Es una palabra alfabetica")
else:
	print("No es una palabra alfabetica")
#---------------------------------------------------------------

#7º Ejercicio
# BUENO

n = int(input("Ingrese un valor: "))
lista_div = []

while True:
	n = int(input("Ingrese un valor: "))
	if n > 0:
		lista_div.append(n)
	elif n <= -1:
		a = max(lista_div)
		print(" El numero mayor es: " + str(a))
		exit()
	else:
		print("Sigue")
#--------------------------------------------------------------

# 8º Ejercicio
# MALO
letra = input(" Escribe tu palabra: ")
num = int(input(" Escribe tu numero: "))
l = len(letra)
k =  num

while True:
	if k > l:
		print("Todas son cortas")
		break
		
	else:
		print("Hay alguna palabra larga")
		break

#--------------------------------------------------------------
# 9º Ejercicio
# BUENO
""" He de reconocer que esté me costo bastante. Tuve que mirar por internet. 
Lo intenté bastante y como siempre, complicando más la solución ó posibles
soluciones que la real"""

cadena = str(input("Escribe una palabra: "))
k = int(input("Escribe un numero: "))
x = cadena.split()
cont = 0

for palabra in x:
	if len (palabra) == k:
		cont = cont + 1
	else:
		print("")
print(" Hay  " +  str( cont ) + " palabras de longitud  " +  str ( k ))



#--------------------------------------------------------------
# 10º Ejercicio
# BUENO
while True:
	p = str(input("Escribe una palabra: "))
	if str (p) == str (p[::-1]):
		print(" Es una palabra palindroma")
	else:
		print("No es una palabra palindroma")
		exit()




		
