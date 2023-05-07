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

import re, os, sys, glob

"""Creá una carpeta llamada “CarpetaParcial” en la que existan 2 archivos .txt que contengan la
siguiente información (los archivo .txt, también tenés que crearlos vos bro):
Contenido del archivo 1:
643262462352362463262+46+423crnewuvpn3t42+3235523+verw+5491142342353532mcw
iromvvwrwrvervwr43v4*3
Contenido del archivo2:
64326246235236bwrbew+54911542263632623r246326vew2+46+423crneevwwuvpnew3tv
ew42+3235523+verw+5491v142342353532mcwiromvvwrwrvervwr43v4*3
Deberás extraer los números de teléfono de CABA (+54911########) y guardarlos en un
archivo nuevo, en una carpeta llamada” Telefonos”, creada dentro de la CarpetaParcial.
Buena suerte!
"""

import re
import os

# Crear la carpeta CarpetaParcial
os.mkdir("CarpetaParcial")

# Crear los archivos .txt con el contenido dado
contenido_archivo1 = "643262462352362463262+46+423crnewuvpn3t42+3235523+verw+5491142342353532mcw\niromvvwrwrvervwr43v4*3"
contenido_archivo2 = "64326246235236bwrbew+54911542263632623r246326vew2+46+423crneevwwuvpnew3tv\new42+3235523+verw+5491v142342353532mcwiromvvwrwrvervwr43v4*3"

with open("CarpetaParcial/archivo1.txt", "w") as archivo1:
    archivo1.write(contenido_archivo1)

with open("CarpetaParcial/archivo2.txt", "w") as archivo2:
    archivo2.write(contenido_archivo2)

# Crear la carpeta Telefonos dentro de CarpetaParcial
os.mkdir("CarpetaParcial/Telefonos")

# Leer los archivos .txt y extraer los números de teléfono
patron_telefono = r'\+54911\d{8}'  # Patrón para encontrar números de teléfono de CABA (+54911########)

for archivo in os.listdir("CarpetaParcial"):
    if archivo.endswith(".txt"):
        ruta_archivo = os.path.join("CarpetaParcial", archivo)
        with open(ruta_archivo, "r") as archivo_txt:
            contenido = archivo_txt.read()
            telefonos = re.findall(patron_telefono, contenido)

            # Guardar los números de teléfono en el archivo nuevo
            ruta_archivo_telefonos = os.path.join("CarpetaParcial/Telefonos", "telefonos_caba.txt")
            with open(ruta_archivo_telefonos, "a") as archivo_telefonos:
                for telefono in telefonos:
                    archivo_telefonos.write(telefono + "\n")

print("Proceso completado.")
