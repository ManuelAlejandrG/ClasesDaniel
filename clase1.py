#print(1+5 +4) ## Sumar
## Restar 
#print(5-4)

""" para un parrafo de comentarios
puedo escribir dentro de esta sección
cualquier tipo de comentario."""


### VARIABLES EN PYTHON 

# VARIABLES NUMÉRICAS

x = 1
a = 2
c = 3

#print(a,c)
# PEP 8 
x = 1.3

a = 2.0
#print(a,x)

#print(type(a))
#print(type(c))

## VARIABLES NO NUMÉRICAS

primera_variable_no_numerica = "No numérico" 
#print(primera_variable_no_numerica)
#print(type(primera_variable_no_numerica))

l = [1,2,3]
#print(l)
#print(type(l))

t = (1,2,3,4)
#print(t)
#print(type(t))

s = {1,2,3,3,3,4,4,1}
#print(s)
#print(type(s))

d = {"uno":1,
	 "dos":2, 
	"tres":3}
#print(d)
#print(type(d))

frutas = ["manzana", "cambur", "pera", "uvas"]

#print(len(frutas))

#print(frutas[2])

# Muestra el último elemento de la lista
#print(frutas[-1])

# Slice 

#print(frutas[0:3])

# 3-0 = 3 elementos

#print(frutas[1:4])

lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


#print(lista_numeros[-1])

#print(lista_numeros[2:-5])
#print(lista_numeros[2:10])


#print(lista_numeros[0:15:2])

#print(lista_numeros[1:15:2])


#print(lista_numeros[:10:3])

#print(lista_numeros[2::4])

#print(lista_numeros[::2])


Nombre = "Manuel Alejandro Goyo"

#print(Nombre[::2])

#print(Nombre[7:16:1])

# Booleanas 

Condicion1 = True
Condicion2 = False

# Métodos de listas 

elementos_carro = ["ruedas", "ventanas", "asientos"]
#print(elementos_carro)
elementos_carro.append("volante")
#print(elementos_carro)

elementos_carro.pop()

#print(elementos_carro)

elementos_carro.remove("ventanas")

#print(elementos_carro[1])


oficina = ["computador","sillas","mesas","pizarra"]

#print(oficina)
oficina.pop(0)
#print(oficina)

#print(oficina[0])
#oficina[0] = "lamparas"

#print(oficina[0])

tup_oficina = tuple(oficina)

#print(tup_oficina)

#tup_oficina[0] = "computador"
#print(tup_oficina[0])

elementos_quimicos = {"O":"Oxigeno", "Au":"Oro","H20":"Agua" }

#print(elementos_quimicos["O"])


edades_personas = {"Juan":24,"Andrea":31, "Andres":15}

mes_cumple_personas = {"Juan":"Septiembre", "Andrea":"Mayo", "Andres":"Febrero"}

print(mes_cumple_personas["Juan"])

print(mes_cumple_personas.keys())
print(mes_cumple_personas.values())

print( type(mes_cumple_personas.keys()))

nombres = list(mes_cumple_personas.keys())
print(nombres)