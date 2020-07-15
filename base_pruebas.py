import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("localhost", "root", "", "libreria")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()

    except Error as e:
        print(f"The error '{e}' occurred")
    return result

"""
select_autores = "SELECT nombre FROM autores"
nombre_autores = execute_read_query(connection, select_autores)

print(nombre_autores)"""
"""
for autor in nombre_autores:
    print(autor)"""

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_libros = """INSERT INTO libros(autor_id, titulo, fecha_publicacion)
VALUES (1, 'Carrie','1974-01-01'),
      (1, 'El misterio de Salmes Lot','1975-01-01'),
      (1, 'El resplando','1977-01-01');"""

execute_query(connection, create_libros)

