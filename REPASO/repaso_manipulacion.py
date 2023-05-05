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
with open('ruta/al/archivo.txt', 'w') as archivo:
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