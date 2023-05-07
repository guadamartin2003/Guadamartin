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

os.mkdir(ruta) # el cual sirve para crear una carpeta en la ruta indicada (si queremos crearla en la carpeta donde estamos parados solo tenemos que poner el nombre de la carpeta).
os.chdir(ruta) # el cual nos permite movernos de carpeta hasta la ruta indicada.

# crear la carpeta Prácticas en el directorio actual:
os.mkdir("Prácticas")

# crear la carpeta Teorías en el directorio superior:
os.mkdir("../Teorías")

# movernos a la carpeta Prácticas:
os.chdir("Prácticas")

# movernos desde Prácticas a Teorías
os.chdir("../../Teorías")

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

#control f para buscar una palabra 
# mi direccion es:     /c/Users/martin/OneDrive/Escritorio/Fundamentos de informatica/informatica_antreassian 

# si dice main es que estoy en mi repo
#en bash pongo git add . // despues pongo git commit -m "y algun comentario aca" // por ultimo pongo git push 
#asi ya subi lo que quiero a mi repo de github 
#chequeo en github que se actualizo mi repo

#os.mkdir(ruta) me permite crear una carpeta. de ruta (entre comillas) le pongo donde la quiero crear. con os.chdir(ruta) me muevo a la carpeta que quiero crear 
#os.mkdir("../Escritorio/carpeta")

#siempre antes de hacer un script pongo #!
#!/usr/bin/env python3 asi le digo que busque y ejecute en la ruta python 

# (../../) PARA moverme a una carpeta de arriba si todavia no estoy ahi. x ejemplo (../../"informes")

#ejercicio de practica

#!

import os
import glob
import sys

# Movemos a la carpeta Informes
os.chdir('Informes')

# Obtenemos los archivos .txt en la carpeta
archivos_txt = glob.glob('*.txt')

# Inicializamos un diccionario para almacenar los resultados
resultados = {}   

# Iteramos sobre cada archivo_txt
for archivo in archivos_txt:

    # Abrimos el archivo
    with open(archivo, 'r') as archivo:

        # Leemos todas las líneas
        lineas = archivo.readlines()

        # Obtenemos la cantidad de líneas
        cantidad_lineas = len(lineas)

        # Obtenemos la cantidad de veces que aparece la palabra 'estado'
    for linea in lineas:
	    if 'estado' in linea:
		    cantidad_estado = cantidad_estado + 1	

        # Guardamos los resultados en el diccionario
resultados[archivo] = (cantidad_lineas, cantidad_estado, lineas[0])

# Creamos la carpeta Apellidos (si no existe)
if not os.path.exists('Apellidos'):
    os.mkdir('Apellidos')

# Creamos el archivo Lista.txt y escribimos la primera línea de cada archivo
with open('Apellidos/Lista.txt', 'w') as f:
    for archivo, (cantidad_lineas, cantidad_estado, primera_linea) in resultados.items():
        f.write(primera_linea)
        f.write('\n')


#Resolucion Guille 

#!/usr/bin/env python3

import os, glob, sys

def ejercicio_rutas():
     os.chdir("Informes")
     txt = glob.glob("*.txt")
     cantidad_estado = []
     cantidad_lineas = []
     for archivo in txt:
          with open(archivo, "r") as file:
               file_completa = file.read()
               cantidad_estado.append(file_completa.count("estado"))
               cantidad_lineas.append(file_completa.count("\n"))

     os.mkdir ("Apellido")
     with open ("Apellido/Lista.txt" , "w") as salida:
        for archivo in txt:
             with open(archivo, "r") as file:
                  #primer_linea = file.readline()
                  #salida.write(primer_linea)
                  salida.write(file.readline())
     return cantidad_estado, cantidad_lineas

c1, c2 = ejercicio_rutas()
