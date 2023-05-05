with open("ejemplo.txt", "r") as f:
    contenido = f.read()
    print(contenido)
"""""
Hola, este es un ejemplo de archivo de texto. 
Este es un archivo de varias líneas. 
Espero que esto te ayude a entender cómo funciona la lectura de archivos en Python.
"""
with open("ejemplo.txt", "r") as f:
    linea = f.readline()
    print(linea)

"Hola, este es un ejemplo de archivo de texto."

with open("ejemplo.txt", "r") as f:
    lineas = f.readlines()
    print(lineas)

['Hola, este es un ejemplo de archivo de texto. \n', 'Este es un archivo de varias líneas. \n', 'Espero que esto te ayude a entender cómo funciona la lectura de archivos en Python.']

with open("ejemplo.txt", "r") as archivo:
    lineas = archivo.readlines()  # lee todas las líneas en una lista
    linea2 = lineas[1]  # obtiene la segunda línea de la lista
    print(linea2)  # muestra la segunda línea por consola

with open("ejemplo.txt", "r") as archivo:
    linea = archivo.readline()
    primeros_cinco_caracteres = linea[:5]

import re

with open('ejemplo.txt', 'r') as f:
    for linea in f:
        if re.findall(r".*[pP].*[rR].*", linea): # devuelve todas las lineas que contengan pr
            print(linea)

import re

with open('ejemplo.txt', 'r') as f:
    for linea in f:
        palabras = linea.split()
        for palabra in palabras:
            if re.search(r".*[pP].*[rR].*", palabra): # devuelve las palabras que contengan pr 
                print(palabra)

import re
with open('ejemplo.txt', 'r') as f:
    for linea in f:
        palabras = linea.split()
        for palabra in palabras:
            coincidencias = re.findall(r"[pPrR][rRpP]", palabra)  # devuelve las palabras que contengan pr o rp si estan juntas
            if coincidencias:
                print(palabra, coincidencias)

#Ejemplo lista de telefonos
"""""
lo hizo guille pero me da error

with open('telefonos.txt', 'r')  as telefonos_validos:
    for linea in telefonos_validos:
        telefonos = linea.split()
        if re.findall( "(+5411)([0-9]{8})", telefonos):
         print(telefonos_validos)

"""
import re

with open('telefonos.txt', 'r')  as telefonos_validos:
    for linea in telefonos_validos: #cumple la misma funcion que read()--- tel= telefonos_validos.read()  lista = find_tel(tel) --se guarda en la variable lista 
        telefonos = linea.split()
        for telefono in telefonos:
            if re.findall(r"\+5411\d{8}", telefono): #r Python no interpretará los caracteres especiales como \n (nueva línea) o \t (tabulación) como lo haría normalmente.
                print(telefono)

#el + se escapa con \ para indicar que se busca el caracter literal +. Luego, 54 y 11 son los números que deben aparecer después del +. Finalmente, \d{8} se refiere a cualquier dígito (\d) que aparezca exactamente 8 veces.