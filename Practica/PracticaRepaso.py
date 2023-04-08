#Ejercicio 1
#Escribí un programa de python que imprima un diccionario cuyas claves sean los números de 1 a 15 y cuyos valores sean las potencias al cuadrado de estos números
# Creamos un diccionario vacío
diccionario = {}

# Iteramos del 1 al 15
for i in range(1, 16):
    # Agregamos una nueva clave-valor al diccionario
    diccionario[i] = i**2

# Imprimimos el diccionario
print(diccionario)

#Ejercicio 2
#Realizá un programa que imprima la suma de todos los valores de un diccionario de números.
# Definimos un diccionario de ejemplo
# Definimos un diccionario de ejemplo
diccionario = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

# Inicializamos una variable para almacenar la suma
suma = 0

# Iteramos a través del diccionario y sumamos los valores
for valor in diccionario.values():
    suma += valor

# Imprimimos el resultado
print("La suma de los valores del diccionario es:", suma)


#Ejercicio 3
#Escribí un programa que obtenga, a partir de una lista de strings una lista con la longitud de esas strings e imprima la longitud de la lista de strings y los elementos de la lista de longitudes
# Definimos una lista de strings de ejemplo
lista_strings = ["Hola", "mundo", "este", "es", "un", "ejemplo"]

# Creamos una nueva lista con las longitudes de las strings
lista_longitudes = [len(s) for s in lista_strings]

# Imprimimos la longitud de la lista original y los elementos de la lista de longitudes
print("Longitud de la lista de strings:", len(lista_strings))
print("Longitudes de las strings:", lista_longitudes)

#Ejercicio 4
#Realizá un programa que a partir de una lista mixta (que contiene distintos tipos de datos) imprima cuántos enteros tiene y además en el caso de los elementos que sean strings hay que crear una nueva lista con estos strings pero reemplazando al A por la U (tanto mayúscula como minúscula) y luego imprimir estos elementos.
# Definimos una lista mixta de ejemplo
lista_mixta = [10, "Hola", 5.6, "AlAzAr", 8, "Ejemplo", True, "Python"]

# Contamos la cantidad de enteros en la lista
enteros = sum(isinstance(x, int) for x in lista_mixta)

# Imprimimos la cantidad de enteros
print("La lista tiene", enteros, "enteros.")

# Creamos una nueva lista con los strings modificados
nueva_lista = [x.replace("A", "U").replace("a", "u") if isinstance(x, str) else x for x in lista_mixta if x]

# Imprimimos los elementos de la nueva lista
print("Nueva lista con strings modificados:", nueva_lista)
