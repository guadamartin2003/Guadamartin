# A) En los textos mágicos .log se encuentra escondido el discurso del sombrero seleccionador.

# Usando todo lo que sabes de las bibliotecas os, glob y re construí un procedimiento que:
# i) cree un directorio cuyo nombre se corresponde con el nombre de la casa elegida,
# la cual se esconde en la 4ta linea del archivo texto5.log.

# ii) extraiga las primeras 4 líneas de los archivos .log

# y las almacene en un único archivo llamado selección_del_sombrero.txt,

# que se guarde en la carpeta creada en el punto i).

import os, glob, re 

def encontrar_discurso(archivo):
    os.mkdir("Gryffindor")                      #creo gryf

    discurso = glob.glob("*.log")               #archivos log 

    for a in discurso:                       # por cada archivo log 

        with open (a, "r") as file:          #abrilo
            palabras = file.readlines()                  #lee las primeras 4 lineas 
            
            with open ("Gryffindor/"+archivo, "a") as file2:            #abri selec
                file2.write(str(palabras[0:4]))

encontrar_discurso("selección_del_sombrero.txt")

# B) Ejecutá el script_misterioso.py y realizá resolvé:

# ¿Qué tipo de exepción arroja la corrida del script? Arroja un ZeroDivisionError: division by zero

# Mejorá el código para que capture dicho error específicamente
# y lo maneje imprimiendo una advertencia al usuario sobre las posibles causas de dicho error

# ¿Qué otras excepciones deberias considerar?