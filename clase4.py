"""def par(entero):

    if entero%2 == 0:
        print(str(entero)+" es un numero par")
    else:
        print(str(entero)+" no es un numero par")
    """
# par(10)


"""
def par2(entero):

    if entero%2 == 0:
        return str(entero)+" es un numero par"
    else:
        return str(entero)+" no es un numero par"
"""

# par(20)


""" 
def pares_no_pares(entero):
    pares = []
    no_pares = []
    for i in range(1,entero+1):
        
        if i%2==0:
            pares.append(i)
            print(str(i)+" es par")
            
        else:
            no_pares.append(i)
            print(str(i)+" es impar")
            
    return pares,no_pares
"""

""" p,n = pares_no_pares(10)
print(p,n)"""

'''
def suma_2_valores(primero, segundo):
    """ Funcion para calcular la suma o la concatenacion de variables
    primero: primera variable puede ser tipo string o tipo float
    segund: segunda variable puede ser tipo string o tipo float
    salida: retorna la suma o concatenacion de primero y segundo """
    
    
    return primero+segundo'''

# suma_2_valores("Hola ", "estoy aprendiendo python")
# suma_2_valores(7,5)

"""
def pares_sin_argument():
    entero = int(input("Ingrese un valor a verificar si es par: "))
    return par2(entero) """


# pares_sin_argument()


""" 
def divisible_3():
    entero = int(input("Ingrese un valor a verificar si es divisible entre 3: "))
    
    if entero%3==0:
        return str(entero)+" si es divisible entre 3"
    else:
        return str(entero)+" no es divisible entre 3"
"""

# divisible_3()


'''
def area_rectangulo():
    """ Esta funcion calcula el area de un rectangulo,
    no pide argumento de entrada pero los argumentos a utilizar se 
    piden por pantalla """
    
    
    
    alto = float(input("Ingrese el valor de la altura del rectangulo: "))
    ancho = float(input("Ingrese el valor de la anchura del rectangulo: "))
    
    return alto*ancho
     ''' 

# area_rectangulo()

"""
def suma_indefinida(*argumento):
    return sum(argumento)"""

# suma_indefinida(1,2,3,531,432,4,642,537,3,36,64,4)


'''
def palindrome():
    """ Funcion para verificar si una oracion es
    un palidrome
    
    Se pide una oracion de entrada y devuelve True si es
    palindrome, ademas imprime si es un palindrome en caso 
    de serlo.
    
    Si la oracion no es palindrome, no hace nada."""
    
    
    # pido por pantalla un texto
    texto = input("Ingrese un texto: ")
    # defino una variable tipo string vacia
    vacio = ""
    # itero sobre texto.split, texto.split() separa el texto
    # en cada espacio y lo convierta una lista
    for i in texto.split():
        # concateno los valores 
        vacio = vacio+i
    
    
    if str(vacio) == str (vacio[::-1]):
        print("Si es un palindrome")
        return True'''


# palindrome 