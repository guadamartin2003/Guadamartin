# FUNCION REPLACE
# Abre el archivo en modo de lectura
with open('archivo.txt', 'r') as f:
    # Lee el contenido del archivo
    contenido = f.read()

# Reemplaza la palabra "archivo" por "documento"
contenido_modificado = contenido.replace('archivo', 'documento')

# Abre el archivo en modo de escritura
with open('archivo.txt', 'w') as f:
    # Escribe el contenido modificado en el archivo
    f.write(contenido_modificado)

#Para cambiar un . por un salto de linea.
with open('archivo.txt', 'r') as f:
    lines = f.readlines()

with open('archivo_modificado.txt', 'w') as f:
    for line in lines:
        line = line.replace(".", "\n")
        f.write(line)

#FUNCION SPLIT

import re

with open('ejemplo.txt', 'r') as f:
    for linea in f:
        palabras = linea.split()
        for palabra in palabras:
            if re.search(r".*[pP].*[rR].*", palabra): # devuelve las palabras que contengan pr 
                print(palabra)

