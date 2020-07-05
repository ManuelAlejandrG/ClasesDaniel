#1º Ejercicio
class Alumno:
   
    def inicializar(self,nom):
        self.nombre=nom
        print("Nombre: ",self.nombre)

""" Primero creo una inicializacion de el atributo con el nombre del alumno.
Como puedes ver arriba. Podríamos poner el nombre que deseemos."""
    def evaluacion(self,eva):
        self.nota = eva
    	if self.nota > 4:
    		print("El alumno {} ha aprobado con la nota {}".format(self.nombre,self.nota))
    	else:
    		print("El alumno {} ha suspendido".format(self.nombre))
""" En esté método doy a elegir la nota que ha sacado el alumno.
Si es mayor que 5, tendrá que salir impreso el 1º mensaje, si 
no el segundo"""
 
 
   

 

persona1 = Alumno()
persona1.inicializar("Marcos")
persona1.evaluacion(3)

#Se imprime los correspondiente al método 
#--------------------------------------------------------------------------------------------
#2º Ejercicio
class Persona:

    def __init__(self, nombre:str, edad:str):
      self.nombre=nombre
      self.edad=edad
      

    def mayor (self):
    	if self.edad >"18":
    		print("{} es mayor de edad".format(self.nombre))

    	else:
    		print("{} es menor de edad".format(self.nombre))



persona1=Persona("Juan","16")
persona2=Persona('Evaristo','20')
persona1.mayor()
persona2.mayor()






#--------------------------------------------------------------------------------------------
# 3º Ejercicio

class Triangulo:
    def __init__(self, lado1,lado2,lado3):
        self.a=lado1
        self.b=lado2
        self.c=lado3
"""En primer lugar creo un método constructor que es el primer
método que se ejecuta cuando se crea un objeto"""

    def operacion(self):
        if self.a != self.b:
            if self.c != self.a:
                print("Triangulo escaleno")
            elif self.c == self.a:
                print("Triangulo isosceles")
        else:
            print("Triangulo Equilatero")
""" En esté método simplemente utilizo los operadores de lógica para que
	cuando sean llamados, realicen la operación exacta"""        
            
primero = Triangulo(13,12,10)
primero.operacion()


#--------------------------------------------------------------------------------------------
# 4º Ejercicio
class Operaciones :

""" Tras probar diferentes posibilidades para introduccir el input,
 busqué por internet, y la que me funcionó fue dando valor NONE."""
    def obterner_datos(self):
        self.x = input("Digito 1: ")
        self.y = input("Digito 2: ")
#Luego cree un método para preguntar al usuario los digitos    
    def sumar(self):
        print( int(self.x) + int(self.y))
    def restar(self):
        print( int(self.x) - int(self.y))
    def multiplicar(self):
       print( int(self.x) * int(self.y))
    def dividir(self):
        print( int(self.x) / int(self.y))
""" En el metodo de operaciones tuve algún que otro problemilla.
Te comento, en un editor no me daba problemas, pero en otros si. Encontré
que debía designar que era numero entero, introduciendo int en las impresiones"""

a = Operaciones()
a.obterner_datos()
a.sumar()
a.restar()
a.multiplicar()
a.dividir()

#--------------------------------------------------------------------------------------------
# 5º Ejercicio

class Menu:
    def imprime(self):
        print("añadir contacto")
        print("Lista contactos")
        print("buscar contacto")
        print("Cerrar agenda")





class Trabajo :
    def __init__(self):
        self.nombre = None
        self.telefono = None
        self.email= None
    def obtener_datos(self):
    	self.nombre=str(input("Introduzca su nombre completo: "))
    	self.telefono=str(input("Introduzca su numero de telefono: "))
    	self.email=str(input("Introduzca su email: "))
    def guardar(self):
        self.contactos= []
        self.contactos.append(self.nombre)
        self.contactos.append(self.telefono)
        self.contactos.append(self.email)
        
        print(self.contactos)


    
        


a=Menu()
a.imprime()
a=Trabajo()
a.obtener_datos()
a.guardar()

#--------------------------------------------------------------------------------------------
# 6º Ejercicio

""" En está parte tuve que guiarme por la solución del ejercicio. Porque al estar trabajando
la idea de hacerlo con input, no supe relazionar una clase con otra clase"""

class Banco:
	# inicializamos
	def __init__(self):
		self.cliente1=Cliente("Ivan")
		self.cliente2=Cliente("Marcos")
		self.cliente3=Cliente("Juan")
 
	# función para operar
	def operacion(self):
		self.cliente1.depositar(1000)
		self.cliente2.depositar(300)
		self.cliente3.depositar(43)
		self.cliente1.extraer(400)
 
	# función para obtener los depósitos totales
	def depositos(self):
		total=self.cliente1.devolver_cantidad()+self.cliente2.devolver_cantidad()+self.cliente3.devolver_cantidad()
		print("El total de dinero del banco es: ",total)
		self.cliente1.imprimir()
		self.cliente2.imprimir()
		self.cliente3.imprimir()
 
 
 
"""Esta parte la pude desarrollar sin mcuhas dificultad.De gecho la estaba preparando
en otra versión, pidiendo input. Pero luego no sabía enlarzarla con la clase banco"""
class Cliente:
	# inicializamos
	def __init__(self,nombre):
		self.nombre=nombre
		self.cantidad=0
 
	# función para depositar dinero
	def depositar(self,cantidad):
		self.cantidad+=cantidad
 
	# función para extraer dinero
	def extraer(self,cantidad):
		self.cantidad-=cantidad
 
	# función para obtener el total de dinero
	def devolver_cantidad(self):
		return self.cantidad
 
	# función para imprimir los datos del cliente
	def imprimir(self):
		print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)
 
 
# bloque principal
banco1=Banco()
banco1.operacion()
banco1.depositos()

#--------------------------------------------------------------------------------------------
# 6º Ejercicio(mi manera)
""" Esta es la versión del ejercicio 6 que no supe relacionar ,después de probar varias
cosas con la clase banco"""

class Operacion:

    def __init__(self):
        self.nombre=str(input("Ingrese su nombre: :"))
        self.cuenta=int(input("En la cuenta hay :"))
        self.depo=int(input("Ingrese su deposito:"))
        self.ext=int(input("Ingrese la cantidad que quiere extraer:"))
        self.mostrar()
        


    def mostrar(self):
        print("Tu nombre:", self.nombre)
        mostrar=self.cuenta+self.depo-self.ext
        print("El total en la cuenta es: ",mostrar)

    def devolver_cantidad(self)
         return self.mostrar



class Banco:
    """docstring for Banco"""
    def __init__(self):
        total=self.total.devolver_cantidad +1
        
        
operacion1=Operacion()

#--------------------------------------------------------------------------------------------


