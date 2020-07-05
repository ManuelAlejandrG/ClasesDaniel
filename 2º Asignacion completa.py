#1º Ejercicio


""" En el primer ejercicio sé que he ido un poco más alla
de lo solicitado en el enunciado; pero tiene una explicacion. 

Al querer probar todo el listado de calificaciones; y para hacerlo
de una forma más dinamica, he introducido : while,bucle de pedir nota 
y break para romper o salir del programa"""

while True:
	cal = float(input(" Introduzca su nota: "))
	if cal > 0:
		if cal < 5:
			print("Suspenso")
			
		elif cal >= 5 and cal < 7:
			print("Aprobado")
			
		elif cal >= 7 and cal < 8.5:
			print("Notable")
			
		elif cal >= 8.5 and cal < 10:
			print("Sobresaliente")
			
		else:
			print("Matricula de honor")
			

	else:
		print("Error, debe ser mayor que 0")
		break


#---------------------------------------------------------------------
#2º Segundo Ejercicio
""" Para que puedas calificar mejor el ejercicio, realicé igualmente 
un bucle y puedas comprobar mejor cada una de las especificaciones"""

""" Seguramente habrá mil formas mejor que resolver este ejercicio
pero para practicar el concepto de la segunda clase se me ocurrió hacerlo así"""

v = str(("a","e","i","o","u"))
v_M = ("A,E,I,O,U")
c = ("z,x,c,v,b,n,m,s,d,f,g,h,j,k,l,q,w,r,t,y,,p")
c_M = ("Z,X,C,V,B,N,M,S,D,F,G,H,J,K,L,Q,W,R,T,Y,P")

while True:
	l = str(input("Introduce la letra: "))
	if l in v:
		print("Es vocal minuscula")
	elif l in v_M:
		print("Es vocal mayuscula")
	elif l in c:
		print("Es consonate minuscula")
	elif l in c_M:
		print("Es cononante mayuscula")
	else:
		print("Has introduccido un nummero, repite por favor")
		break




#---------------------------------------------------------------------
#3º Ejercicio

while True:
	p = int(input(" Edad de la primera persona: "))
	s = int(input(" Edad de la segunda persona: "))
	try:
		if p > s:
			print (" La primera persona es mayor que la segunda")
		elif s > p:
			print("La segunda persona es mayor que la primera")
		elif p == s:
			print("Son de la misma edad")
		else:
			print("ERROR: Revise los numeros")
	except ValueError:
		
		""" Intenté buscar una solución en caso
		que el usuario agregase letras en vez de números
		raise ValueError, ("x e y deben poder convertirse a enteros")"""

#---------------------------------------------------------------------

#4º Ejercicio
""" En esté ejercicio lo he podido hacer de dos formas. La primera con 
la funcion min"""

while True:
	v1 = int(input("Primer valor: "))
	v2 = int(input("Segundo valor: "))
	v3 = int (input("Tercer valor: "))

	#m = min(v1,v2,v3)
	#print(m)
	
	if v1<v2<v3:
		print("Primer valor es el más pequeño")
	elif v2<v1<v3:
		print("Segundo valor es más pequeño ")
	else:
		print("Tercer valor es más pequeño")
		exit()
#---------------------------------------------------------------------
#5º Ejercicio
while True:
	num = int(input(" Introduce tu numero"))
	if num%2 == 0:
		print(" El nuero es par")
	else:
		print(" El numero es impar")
		exit()
#---------------------------------------------------------------------
#6º Ejercicio
while True:
	num = int(input("Introduce tu numero: "))
	if (num/2) % 2 != 0:
		print (num, "es el doble de ", int(num/2), " que es impar")
	else:
		print ( "numero par")
#---------------------------------------------------------------------

#7º Ejercicio
while True:
	euros = int(input(" Cuantos euros son el capital: "))
	intereses = int(input("interes: "))
	anos = int(input("Cuantos anos: "))
	e = int(euros)
	inte = int(intereses)
	a = int(anos)
	cantidad = e * (1 + inte/100)**a

	if cantidad > 0:
		print(cantidad)
	else:
		print("Numero negativo.ERROR")
#---------------------------------------------------------------------
#8º Ejercicio
while True:
	a = int(input(" Introduzca el numero del mes: "))
	if a >= 0 and a<=3:
		print("Meses de invierno")
	elif a >= 4 and a <=6:
		print(" Meses de primavera")
	elif a>=7 and a<=9 :
		print("MEses de verano")
	elif a >=10 and a<=12:
		print("Meses de otoño")
	elif a<0 and a<-1:
		print("Numero negativo")
	else:
		print ("Revise lo escrito")
		exit()
#---------------------------------------------------------------------
#9 Ejercicio
while True:
	ano = int(input("Introduzca el ano: "))
	if ano % 4:
		if ano % 400:
			print("Año bisiesto")
		else:
			print ("Año no bisiesto")
	else:
		print (" año no bisiesto")
		exit()


