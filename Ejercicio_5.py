# 1º Ejercicio
class Alumno:

    def inicializar(self, nom):
        self.nombre = nom
        print("Nombre: ", self.nombre)

    """ Primero creo una inicializacion de el atributo con el nombre del alumno.
    Como puedes ver arriba. Podríamos poner el nombre que deseemos."""


    def evaluacion(self, eva):
        self.nota = eva
        if self.nota > 4:
            print("El alumno {} ha aprobado con la nota {}".format(self.nombre, self.nota))
        else:
            print("El alumno {} ha suspendido".format(self.nombre))

    """ En esté método doy a elegir la nota que ha sacado el alumno.
    Si es mayor que 5, tendrá que salir impreso el 1º mensaje, si 
    no el segundo"""

# 1º Ejercicio
class Alumno_modificado:

    def __init__(self, nom):
        self.nombre = nom
        print("Nombre: ", self.nombre)

    """ Primero creo una inicializacion de el atributo con el nombre del alumno.
    Como puedes ver arriba. Podríamos poner el nombre que deseemos."""


    def evaluacion(self, eva):
        self.nota = eva
        if self.nota > 4:
            print("El alumno {} ha aprobado con la nota {}".format(self.nombre, self.nota))
        else:
            print("El alumno {} ha suspendido".format(self.nombre))

    """ En esté método doy a elegir la nota que ha sacado el alumno.
    Si es mayor que 5, tendrá que salir impreso el 1º mensaje, si 
    no el segundo"""




persona1 = Alumno()
persona1.inicializar("Marcos")
persona1.evaluacion(3)

persona1 = Alumno_modificado("Marcos")
persona1.evaluacion(3)