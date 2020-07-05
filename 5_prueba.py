class Operacion:

    def __init__(self):
        self.nombre = str(input("Ingrese su nombre: :"))
        self.cuenta = int(input("En la cuenta hay :"))
        self.depo = int(input("Ingrese su deposito:"))
        self.ext = int(input("Ingrese la cantidad que quiere extraer:"))
        self.mostrar()

    def mostrar(self):
        print("Tu nombre:", self.nombre)
        mostrar = self.cuenta + self.depo - self.ext
        print("El total en la cuenta es: ", mostrar)

    def devolver_cantidad(self):
        return self.mostrar


class Banco:
    """docstring for Banco"""

    def __init__(self):
        total = self.total.devolver_cantidad + 1


operacion1 = Operacion()
#banco1 = Banco()