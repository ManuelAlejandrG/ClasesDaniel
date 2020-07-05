## Bucles o Iteracion


# Bucles indeterminados (WHILE)

"""n = 0 
while n<5:
  print(n)
  n = n+1

print("Fin del programa")
"""
"""
n = 1 
while n%10!=0:
  print(n)
  n = n+1"""
"""

condicion = 0
while condicion not in [1,2,3]:
  condicion = int(input("Ingrese una opcion "))

  if condicion==1:
    print("primera opcion")

  elif condicion==2:
    print("segunda opcion")

  elif condicion==3:
    print("tercera opcion")

  else:
    print("Ingresaste una opcion invalida, seleccione de nuevo")

"""
"""
from math import pi 

opcion = 0

while opcion not in [1,2,3]:

  radio = input("Ingrese el valor del radio ")

  opcion = (input("Pulse 1) si desea calcular diametro, 2) si desea calcular perimetro y 3) si desea calcular el area "))

  if int(opcion) == 1:
    print("el diametro es: ")
    print(2*float(radio))

  elif int(opcion) ==2 :
    print("el perimetro es: ")
    print(2*pi*float(radio))


  elif int(opcion)==3:
    print("el area es: ")
    print(pi*(float(radio)**2))

  else:
    print("valor invalido")
    print("ingrese un valor entre 1,2 y 3") """



# Bucles determinados (FOR)

"""
for variable in [1,2,3]:
  print(variable*2)
"""

"""
for variable in [1,2,3,4,5,6,7,8,9,10]:
  print(variable)"""


"""
for i in range(80):
  print(i)"""

"""
i=0
while i < 80:
  print(i)
  i = i+1"""


"""for i in range(1,80,2):
  print(i)

"""
"""
i=1
while i < 80:
  print(i)
  i = i+2"""

"""
articulos = ["harina", "maiz", "manzana", "aceite"]


for i in articulos:
  print("Voy a compar "+ (i))
"""

"""
for i in range(len(articulos)):
  print("Voy a comprar "+articulos[i])"""



"""
n = int(input("Ingrese un valor: "))
lista_div = []

for i in range(1,n+1):

  if n%i == 0:
    lista_div.append(i)

print(lista_div)"""


"""
n = int(input("Ingrese un valor: "))
lista_div = []

for i in range(1,n+1):

  if n%i == 0:
    lista_div.append(i)

if len(lista_div)==2:
  print(str(n)+" es un numero primo")

else:
  print(str(n)+" no es un numero primo")

"""

"""
n = int(input("Ingrese un valor: "))
lista_div = []

for i in range(1,n):

  if n%i == 0:
    lista_div.append(i)

if sum(lista_div) ==n:
  print(str(n)+ " es un numero especial")

else:
    print(str(n)+ " no es un numero especial")"""


"""lista_n = [1,2,3,4,64,62,47735,75,74]

## Hallar la suma de los elementos sin usar la funcion sum()

s = 1
for i in lista_n:
  s = i *  s
  

print(s)
"""

"""
n = int(input("Ingrese un valor "))

if n==0:
  fact = 1

else:
  fact = 1
  for i in range(1,n+1):
    fact = i * fact

print(fact)

"""
n = int(input("Ingrese un valor "))

lista_par = []
lista_tres = []

lista_cinco = []

lista_siete = []

for i in range(1,n+1):

  if i%2==0:
    lista_par.append(i)

  elif i%3==0:
    lista_tres.append(i)

  elif i%5==0:
    lista_cinco.append(i)

  elif i%7==0:
    lista_siete.append(i)

print(lista_par)
print(lista_tres)
print(lista_cinco)
print(lista_siete)


Hackerrank 