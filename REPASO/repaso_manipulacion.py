#Para abrir un archivo de texto, ya sea para usarlo o escribir en el, podemos usar la función nativa de Python open():

path_al_archivo= "el archivo que quiero"
modo= "r, w , a , rb"
open(path_al_archivo, modo) 
archivo = open('ruta/al/archivo.txt', 'r') #modo lectura
archivo = open('ruta/al/archivo.txt', 'w') #modo escribir
archivo = open('ruta/al/archivo.txt', 'r+') #modo lectura y escritura
archivo = open('ruta/al/archivo.txt', 'a') # modo agregado
archivo = open('ruta/al/archivo.jpg', 'rb') #modo binario

#Abrir un archivo para escritura y crearlo si no existe:
with open('ruta/al/archivo.txt', 'w') as archivo: #archivo palabra que uso para referirme al archivo que abro
    # hacer algo con el archivo

#Abrir un archivo para escritura y borrar su contenido previo:
with open('ruta/al/archivo.txt', 'w') as archivo:
    archivo.write('nuevo contenido')

#Abrir un archivo para lectura:
with open('ruta/al/archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

#Abrir un archivo para agregar contenido al final:
with open('ruta/al/archivo.txt', 'a') as archivo:
    archivo.write('contenido adicional')

#Si se desea escribir en el archivo, se sobrescribirá a partir de la posición actual del puntero.
with open("mi_archivo.txt", "r+") as f:
    print(f.read())
    f.write("nuevo texto")
    f.seek(0)
    print(f.read())

#Esta biblioteca del sistema operativo de Python proporciona funciones para interactuar con el sistema operativo. Esta incluye métodos que como os.getcwd() o os.chdir(), que nos permitirá conocer el directorio de trabajo o cambiar de directorio de forma automática:

import os
os.getcwd()
'/home/Ana'
os.chdir('/home/Ana/Documents')
os.getcwd()
'/home/Ana/Documents'

#Por ejemplo, para crear un nuevo directorio llamado "nuevo_directorio" en la carpeta actual, podemos hacer lo siguiente:
import os
os.mkdir("nuevo_directorio")

#Por otro lado, os.listdir() es una función que se utiliza para obtener una lista de todos los archivos y subdirectorios en un directorio determinado.
os.listdir(path)

#definir un procedimiento que lea los archivos .txt que esten en la carpeta de marzo,
# y copie la primera linea de cada uno en un archivo dentro de la carpeta resulados
#(que debe estar dentro de new) 


#!-/usr/bin/en python3
import os, glob, sys

def primeras_lineas(path_a_txt, path_resultado, salida):
    #movemos a marzo
    #extraemos los .txt
    #leemos las primeras primeras_lineas
    #hacemos carpeta de salida (resultado)
    #hacer archivo (salida.txt)
    #poner lineas en archivo nuevo
    os.chdir(path_a_txt) # cambia el directorio de trabajo a la carpeta especificada en 'path_a_txt'
    textos = glob.glob("*.txt") # crea una lista con los nombres de todos los archivos .txt en la carpeta actual
    primer_linea = [] # inicializa una lista vacía para guardar las primeras líneas de cada archivo
    for txt in textos: # recorre todos los archivos .txt en la carpeta actual
        with open(txt, "r") as texto: # abre cada archivo en modo lectura
            primer_linea.append(texto.readline()) # lee la primera línea de cada archivo y la agrega a la lista 'primer_linea'
    os.chdir("../../") # cambia el directorio de trabajo dos niveles hacia atrás
    os.mkdir(path_resultado) # crea una carpeta con el nombre especificado en 'path_resultado'
    with open(salida, "a") as final_txt: # abre un archivo en modo append, con el nombre especificado en 'salida'
        for linea in primer_linea: # recorre todas las primeras líneas guardadas en 'primer_linea'
            final_txt.write(linea) # escribe cada línea en el archivo 'final_txt'

#glob.glob("*.txt") es una función que busca en un directorio actual (o en otro directorio especificado) todos los archivos que tienen extensión .txt.
#La función devuelve una lista de todos los nombres de archivo que coinciden con el patrón de búsqueda "*.txt".
#Por lo tanto, textos es una lista de todos los nombres de archivo que terminan en .txt que se encuentran en el directorio actual.

primeras_lineas("datos/marzo", "resultado", "salida.txt")

#clase teorica 20/3

#!/bin/python3

with open("mi_nombre.txt", "a") as mi_arch:
    mi_arch.write("Ana Julia Velez Rueda")

#tarea: armar un script que lea el archivo "un_arch.txt" y me cree otro archivo "nuevo_arch.txt" con los primeros 5 caracteres del archivo que leimos

#with open("un_archivo.txt", "r") as mi_arch:
    #with open("nuevo_archivo.txt", "a") as nuevo:
        #nuevo.write(mi_arch.readline(5))


texto_leido = open ("un_archivo.txt", "r").read()

texto_para_escribir = texto_leido[0:6]

with open("nuevo_archivo.txt", "a") as mi_arch:
    mi_arch.write(texto_para_escribir)

import os
os.rename("nombre_archivo1", "nombre_archivo2" + ".temp")
os.rename("nombre_archivo2", "nombre_archivo1")
os.rename("nombre_archivo2.temp", "nombre_archivo2")

