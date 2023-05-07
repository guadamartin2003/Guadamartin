#definir un procedimiento que lea los archivos .txt que esten en la carpeta de marzo,
# y copie la primera linea de cada uno en un archivo dentro de la carpeta resulados
#(que debe estar dentro de new) 

#!-/usr/bin/en python3
import os, glob, sys

def primeras_lineas(path_a_txt, path_resultado, salida):
    
    os.chdir(path_a_txt) #change direcory  #movemos a marzo

    textos=glob.glob("*.txt") #extraemos los .txt
    
    primer_linea = []   #leemos las primeras primeras_lineas
    
    for txt in textos:
    
        with open(txt, "r") as texto:
    
            primer_linea.append(texto.readline())
    
    os.chdir("../../") # para moverse para atras 2 veces
    
    os.mkdir(path_resultado) #hacemos carpeta de salida (resultado)
    
    with open(salida, "a") as  final_txt: #hacer archivo (salida.txt)
    
        for linea in primer_linea:
    
            final_txt.write(linea)   #poner lineas en archivo nuevo

primeras_lineas("datos/marzo", "resultado", "salida.txt")


    
     


