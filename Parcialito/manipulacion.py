# Consigna 2 A

# Construir un programa que LEA los archivos .txt y extraiga todas las cuentas de gmail de los agentes secretos
# y las almacene en un único archivo base_de_datos.txt .

# Usá todo lo que sabes de las bibliotecas os, glob y re

import re, os, glob

def filtrar(archivo):           #archivos de salida, el que tenemos que crear

    textos = glob.glob("*.txt")

    with open (archivo, "a") as arch:
        for archivo in textos:
            with open(archivo, "r") as archivo_secreto:
                texto = archivo_secreto.read()
                lista = re.findall("[\w]+[-_\.]*[\w]+@gmail.com", texto)
                for email in lista:
                    arch.write(email + "\n")
                
filtrar("base_de_datos.txt")

# Consigna 2 B --> en script.misterioso.py 