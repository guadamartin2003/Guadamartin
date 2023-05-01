# Ejercicio 1
# Definir un procedimiento que tome como parámetro una lista, verifique si tiene el elemento "control" y le agregue el string "revisado" y le quite el elemento "control".

def verificar_control(lista):
    if "control" in lista: #Si 'control es un elemento dentro de la lista'
        indice = lista.index("control") # lista.index("control") devuelve la posicion en la que aparece 'control' y almacena en la var local
        lista[indice] = "control revisado" #Modifica el elemento el la paosición en la que se encontraba control.
        # lista.remove("control") 

mi_lista_2 = ['control',1,2,3,4]
verificar_control(mi_lista_2)
# print(mi_lista_2)

# Ejercicio 2
# Definir un procedimiento que tome una lista como parámetro y elimine el primer elemento de la lista. Hacer las verificaciones que sean necesarias.
mi_lista = [1, 2, 3, 4, 5]

def eliminar_primer_elemento(lista):
    if len(lista) > 0:
        lista.pop(0) #para eliminar y devolver un elemento de una posición específica de la lista. Pasar como parámetro el elemnto a eliminar
    else:
        print("La lista está vacía")

eliminar_primer_elemento(mi_lista)
# print(mi_lista)

#ALTERNATIVA utilzar 'del' Ej: ---- del lista[0] ----  Se puede utilizar para eliminar elementos de listas, diccionarios y otros objetos.

# Ejercicio 3
# Definir una función que dada una lista y un elemento devuelva la posición de este elemento en la lista

def posicion_elemento(lista,elemento):
    posicion = -1
    for element in lista:
        posicion+=1
        if elemento == element:
            return 'posición: '+str(posicion)
        # ALTERNATIVA --- list.index() --- busca el índice de un elemento en una lista. (Primera aparición del elemento en la lista)
# print(posicion_elemento([1,2,3,4,3], 3))

# Ejercicio 4
# Definir un procedimiento que tome como parámetros dos listas y un elemento, en la que se debe eliminar el elemento de una lista y agregarlo a la otra. Realizar dos versiones del ejercicio, usando un método distinto para eliminar el elemento en cada versión. ¿Qué problema/s tiene este procedimiento?

# MODELO 1
def eliminar_y_agregar(lista1,lista2,elemento):
        if elemento in lista1:
            lista2.append(elemento)
            del lista1[lista1.index(elemento)] #ALTERNATIVA -- BORRAR ELEMENTO CON .pop(list.index(elemento)) --

# MODELO 2
def eliminar_y_agregar2(lista1,lista2,elemento):
    if elemento in lista1:
        lista1.remove(elemento)
        lista2.append(elemento)

lista1 = [1,2,3]
lista2 = [4,5,6]
eliminar_y_agregar(lista1,lista2,1)
# print(lista1,lista2)
            


# Ejercicio 5
# Escribir una función que tome como parámetro una lista de enteros y devuelva una lista con valores booleanos que indique si cada elemento es par o impar. Por ejemplo, para la lista [2, 45, 108, 12, 7], la función debería retornar [True, False, True, True, False]. 

# Utilizar la función realizada en la práctica anterior.
# NO ENTENDI CUAL FUNCIÓN USAR.

def par_impar(lista):
    for numero in lista:
        posicion = lista.index(numero)
        lista[posicion] = (numero%2 == 0)
    return lista

def par_impar2(lista):
    return [(num % 2 == 0) for num in lista]  #En lugar de cambiar el valor de cada elemento por un booleano, devuelve una lista nueva co booleanos.

# print(par_impar([1,2,3,4,5]))

# Ejercicio 6
# Escribir una función que lea un string y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).

def cant_por_caracter(string):
    caracteres ={}
    for caracter in string:
        if caracter in caracteres:
            caracteres[caracter] += 1
        else:
            caracteres[caracter] =1
    return caracteres

# print(cant_por_caracter('Habia'))

# Ejercicio 7
# Modificá la función anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.

# DUDA --> COMO HACERLO PARA NO TENER QUE CREAR UN DICCIONARIO CON TODOS LOS CARACTERES.

# Ejercicio 8
# Definir una función que dada una palabra, nos diga si el palíndromo o no.

def palabra_palindroma(string):
    return string.lower() == string.lower()[::-1]

# print(palabra_palindroma('asdssa'))

# Ejercicio 9
# Definir una función llamada productoria que toma como parámetro una lista de números y los multiplica a todos.

def productoria(lista):
    producto = 1
    for numero in lista:
        nuevo_prod = producto * numero
        producto = nuevo_prod
    return producto

# print(productoria([200,25,43345]))

# Ejercicio 10
# Creá un programa para gestionar datos de los socios de un club, el cual permita:

# Cargar la información de los socios en un diccionario, al cual poder acceder por número de socio. Los datos que se deben almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al dia (s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

# Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día

# Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día

# Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día

# Informar la cantidad de socios que tiene el club.

# Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.

# Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.

# Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).

# Imprimir el listado de socios completos.

# Definir las funciones y/o procedimientos que creas necesarios.

socios = {
    1: {"nombre": "Florencia", "apellido": "Ocampo", "fecha_ingreso": "14/09/2001", "cuota_al_dia": True},
    2: {"nombre": "David", "apellido": "Estévez", "fecha_ingreso": "14/09/2001", "cuota_al_dia": True},
    3: {"nombre": "Sofía", "apellido": "Cáceres", "fecha_ingreso": "14/09/2001", "cuota_al_dia": True},
    4: {"nombre": "Lionel", "apellido": "Messi", "fecha_ingreso": "21/10/2017", "cuota_al_dia": True}
}
# CANTIDAD DE SOCIOS
def cant_socios(diccionario):
    return len(diccionario)
# print(len(socios)) -- SABER CANTIDAD DE SOCIOS --

# REVISAR PAGO CUOTA
def revisar_pago(numero_socio):
    return socios[numero_socio]['cuota_al_dia']
# print(revisar_pago(3))

# CAMBIO FECHA
def cambio_fecha(fecha1, fecha2):
    for socio in socios:
        if socios[socio]['fecha_ingreso'] == fecha1:
            socios[socio]['fecha_ingreso'] = fecha2
# cambio_fecha('21/10/2017','22/10/2017')
# print(socios)

def dar_de_baja(nombre, apellido):
    for numero_socio, datos in socios.items(): # Ciclo for recorre dicc -socios- con método .items() retorna una lista de tuplas donde cada tupla contiene la clave y el valor correspondiente al elemento del diccionario.
        if datos["nombre"] == nombre and datos["apellido"] == apellido:
            del socios[numero_socio]
            break
    else:
        print("No se encontró al socio") #PARA CERRAR BUCLE FOR POR SI LOS DATOS FUERON MAL INGRESADOS O NO EXISTE EL SOCIO
# dar_de_baja('Florencia','Ocampo')
# print(socios)