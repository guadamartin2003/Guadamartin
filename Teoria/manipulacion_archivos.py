# # Ejercicio 1
# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una 
# determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

contador = 0
ruta_archivo = 'C:/Users/salva/Desktop/fundamentos_inf/fi_ucema_burgos/practicas/texto_prueba.txt'
def empieza_con_letra(letra):
    global contador
    with open(ruta_archivo,'r') as archivo:
        for linea in archivo:
            if not linea.startswith(letra.lower() or letra.upper()):
                contador+=1
empieza_con_letra('p')
# print(contador)

#ALTERNATIVA GUILLERMO PRÁCTICA

def start_with(letra,archivo):
    count = 0
    with open(archivo,"r") as file:
        for line in file:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                count += 1

# Ejercicio 2
# Escribí un programa que lea un archivo e imprima las primeras n líneas.
def leer_n_lineas(cantidad,archivo):
    with open(archivo,'r') as file:
        for i in range(cantidad):
            print(file.readline())

# print(leer_n_lineas(1,'C:/Users/salva/Desktop/fundamentos_inf/fi_ucema_burgos/practicas/texto_prueba.txt'))

# Ejercicio 3
# Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

def imprimir_ultimas(cantidad,archivo):
    with open(archivo,'r') as file:
        print(file.readlines()[-cantidad:])

# imprimir_ultimas(4,'C:/Users/salva/Desktop/fundamentos_inf/fi_ucema_burgos/practicas/texto_prueba.txt')

#ALTERNATIVA GUILLERMO PRÁCTICA 

def read_n_back_lines(n,archivo):
    texto = open(archivo,'r').readlines()
    for i in range((len(texto)-n),len(texto)):
        print(texto[1])

# read_n_back_lines(2,'documento')

# Ejercicio 4
# Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def cantidad_palabras(archivo):
    palabras = 0
    with open(archivo,'r') as file:
        for line in file:
            linea = line.split()
            for palabra in linea:
                palabras +=1
    print(palabras)
# print(cantidad_palabras('C:/Users/salva/Desktop/fundamentos_inf/fi_ucema_burgos/practicas/texto_prueba.txt'))

#ALTERNATIVA

def contar_palabras(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()
        pal = contenido.split()
        cantidad_palabra = len(pal)
        print(archivo,cantidad_palabra)

# Ejercicio 5
# Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

def reemplazar(entrada, salida, letra):
    with open(entrada, 'r') as file, open(salida, 'w') as file2:
        for line in file:
            file2.write(line.replace(letra, letra + '\n'))  #Reemplazo y lo escribo en el nuevo archivo
    # reemplazar('sin_saltos.txt', 'texto_prueba.txt','n')

# Ejercicio 6
# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

def eliminar_saltos(archivo):
    sin_saltos = ''
    with open(archivo,'r') as file1, open('./fi_ucema_burgos/practicas/sin_saltos.txt','w') as file2:
        for linea in file1:
            sin_saltos+=linea[:-1]
        file2.write(sin_saltos)
# eliminar_saltos('C:/Users/salva/Desktop/fundamentos_inf/fi_ucema_burgos/practicas/texto_prueba.txt')

# Ejercicio 7
# Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

def palabra_larga(archivo):
    mas_larga = 0
    palabra_larga = ''
    with open(archivo,'r') as file:
        for palabra in file.read().split():
            if len(palabra)>mas_larga:
                mas_larga=len(palabra)
                palabra_larga=palabra
        print('caracteres:', mas_larga, 'palabra:', palabra_larga)

# palabra_larga('C:/Users/salva/Desktop/fundamentos_inf/fi_ucema_burgos/practicas/texto_prueba.txt')

# ALTERNATIVA GUILLERMO PRÁCTICA

def longest_word(archivo):
    max_long=0
    palabra=''
    with open(archivo,'r') as f:
        word_list = f.read().split()
        for word in word_list:
            if len(word)>max_long:
                max_long=len(word)
                palabra=word
    print("La palabra mas larga es: " + palabra)

# Ejercicio 8
# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

def juntar_contenido(archivo1,archivo2,archivo3):
    with open(archivo1,'r') as file1, open(archivo2,'r') as file2, open(archivo3,'a') as file3:
        file3.write(file1.read()+file2.read())

# juntar_contenido('fi_ucema_burgos/practicas/sin_saltos.txt','fi_ucema_burgos/practicas/texto_prueba.txt','fi_ucema_burgos/practicas/ej8prueba.txt')

# ALTERNATIVA GUILLERMO PRÁCTICA

def join_files(file1,file2,file3):
    with open(file1,'r') as f1, open(file2,'r') as f2, open(file3,'a') as f3:
        f3.write(f1.read()+f2.read())

# Ejercicio 9
# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

def frecuencia_palabra(archivo):
    diccionario = {}
    palabras =0
    with open(archivo,'r')as file:
        for line in file:
            linea = line.split()
            for palabra in linea:
                palabras +=1
                if palabra not in diccionario:
                    diccionario[palabra] = 1/palabras
                else:
                    diccionario[palabra]+=1/palabras
        print(diccionario)

# frecuencia_palabra('fi_ucema_burgos/practicas/texto_prueba.txt')


# Ejercicio 10
# Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.