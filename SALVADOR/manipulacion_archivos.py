# # Ejercicio 1
# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una 
# determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

contador = 0
ruta_archivo = 'C:/Users/salva/Desktop/fundamentos_inf/fi_ucema_burgos/practicas/texto_prueba.txt'
def empieza_con_letra(letra):
    global contador # indicamos que la variable 'contador' está definida fuera de la función y se puede modificar dentro de ella
    with open(ruta_archivo,'r') as archivo: # abrimos el archivo en modo lectura con 'with' para asegurarnos de cerrarlo automáticamente
        for linea in archivo: # leemos línea por línea del archivo
            if not linea.startswith(letra.lower() or letra.upper()): # comprobamos si la línea no comienza con la letra (pasada como argumento) en minúscula o mayúscula
                contador += 1 # si no comienza con la letra, incrementamos el contador

empieza_con_letra('p')

def lineas_no_coincidentes(archivo, letra):
    contador = 0
    with open(archivo, 'r') as f: # Abrimos el archivo en modo lectura
        for linea in f:
            if not linea.startswith(letra):
                contador += 1
    return contador
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
def leer_n_lineas(cantidad, archivo):
    with open(archivo,'r') as file:# Abre el archivo en modo lectura y lo asigna a la variable "file".
         for i in range(cantidad):# Itera sobre los primeros "cantidad" de líneas del archivo.
            print(file.readline())# Imprime la línea actual.

# print(leer_n_lineas(1,'C:/Users/salva/Desktop/fundamentos_inf/fi_ucema_burgos/practicas/texto_prueba.txt'))

# Ejercicio 3
# Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

def imprimir_ultimas(cantidad, archivo):
    with open(archivo, 'r') as file: # Abrimos el archivo en modo lectura
        lineas = file.readlines()   # Leemos todas las líneas del archivo y las almacenamos en la variable 'lineas'
        ultimas = lineas[-cantidad:] # Obtenemos las últimas 'cantidad' líneas del archivo 
        print(ultimas)              # Imprimimos las últimas líneas obtenidas
 #lineas[-cantidad:] significa que se toman los elementos desde la posición -cantidad  hasta el final de la lista. 
 #[:cantidad] mostraría las primeras cantidad líneas del archivo en lugar de las últimas.
 #[cantidad:] significa que toma todas las posiciones de la lista desde la posición cantidad hasta el final.
# print(imprimir_ultimas(4,'C:/Users/salva/Desktop/fundamentos_inf/fi_ucema_burgos/practicas/texto_prueba.txt'))

#ALTERNATIVA GUILLERMO PRÁCTICA 

def read_n_back_lines(n,archivo):
    texto = open(archivo,'r').readlines()
    for i in range((len(texto)-n),len(texto)):
        print(texto[1])

# read_n_back_lines(2,'documento')

# Ejercicio 4
# Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def cantidad_palabras(archivo):
    palabras = 0                  # Inicializa el contador de palabras en 0
    with open(archivo,'r') as file:  # Abre el archivo en modo lectura
        for line in file:            # Itera sobre cada línea del archivo
            linea = line.split()     # Divide la línea en palabras usando el método split()
            for palabra in linea:    # Itera sobre cada palabra de la línea
                palabras +=1         # Incrementa el contador de palabras
    print(palabras)                 # Imprime el número total de palabras

# print(cantidad_palabras('C:/Users/salva/Desktop/fundamentos_inf/fi_ucema_burgos/practicas/texto_prueba.txt'))

#ALTERNATIVA

def contar_palabras(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()
        pal = contenido.split()
        cantidad_palabra = len(pal)
        print(archivo,cantidad_palabra)

# Ejercicio 5
def reemplazar(entrada, salida, letra):
    # Abrimos el archivo de entrada en modo lectura y el archivo de salida en modo escritura
    with open(entrada, 'r') as file, open(salida, 'w') as file2:
        # Recorremos cada línea del archivo de entrada
        for line in file:
            # Reemplazamos la letra por la letra más un salto de línea en la línea actual
            # y escribimos la línea resultante en el archivo de salida
            file2.write(line.replace(letra, letra + '\n'))   #Reemplazo y lo escribo en el nuevo archivo
    # reemplazar('sin_saltos.txt', 'texto_prueba.txt','n')

# Ejercicio 6
# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

def eliminar_saltos(archivo):
    # Creamos una variable para guardar el contenido del archivo sin saltos de línea
    sin_saltos = ''
    # Abrimos el archivo original en modo lectura y el archivo nuevo en modo escritura
    with open(archivo,'r') as file1, open('./fi_ucema_burgos/practicas/sin_saltos.txt','w') as file2: #Esta línea de código está abriendo un archivo llamado sin_saltos.txt en el modo de escritura ('w') y asignándolo a la variable file2. El argumento './fi_ucema_burgos/practicas/sin_saltos.txt' indica la ruta y el nombre del archivo que se va a crear o sobrescribir si ya existe.
        # Recorremos cada línea del archivo original
        for linea in file1:
            # Agregamos cada línea sin el salto de línea al contenido sin_saltos
            sin_saltos+=linea[:-1] #[:-1] para obtener la porción de la línea desde el primer caracter hasta el penúltimo, eliminando así el último caracter que es el salto de línea.
        # Escribimos el contenido sin_saltos en el archivo nuevo
        file2.write(sin_saltos)

# eliminar_saltos('C:/Users/salva/Desktop/fundamentos_inf/fi_ucema_burgos/practicas/texto_prueba.txt')

# Ejercicio 7
# Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

def palabra_larga(archivo):
    mas_larga = 0 # inicializa una variable para guardar la longitud de la palabra más larga encontrada
    palabra_larga = '' # inicializa una variable para guardar la palabra más larga encontrada
    with open(archivo,'r') as file: # abre el archivo en modo lectura
        for palabra in file.read().split(): # lee el archivo, separando las palabras y las itera una a una
            if len(palabra)>mas_larga: # si la longitud de la palabra actual es mayor que la longitud de la palabra más larga encontrada hasta el momento
                mas_larga=len(palabra) # actualiza la longitud de la palabra más larga encontrada
                palabra_larga=palabra # actualiza la palabra más larga encontrada
        print('caracteres:', mas_larga, 'palabra:', palabra_larga) # imprime la longitud y la palabra más larga encontrada


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

# La función recibe como parámetros los nombres de tres archivos: archivo1 y archivo2 que se quieren combinar, y archivo3 en el que se va a guardar el resultado.
def juntar_contenido(archivo1,archivo2,archivo3):
    
    # Se abre el primer archivo en modo de lectura, se lo asocia a la variable file1
    # Se abre el segundo archivo en modo de lectura, se lo asocia a la variable file2
    # Se abre el tercer archivo en modo de escritura, se lo asocia a la variable file3
    with open(archivo1,'r') as file1, open(archivo2,'r') as file2, open(archivo3,'a') as file3:
        
        # El contenido de los archivos 1 y 2 se lee y se concatena y se guarda en file3
        file3.write(file1.read()+file2.read())


# juntar_contenido('fi_ucema_burgos/practicas/sin_saltos.txt','fi_ucema_burgos/practicas/texto_prueba.txt','fi_ucema_burgos/practicas/ej8prueba.txt')

# ALTERNATIVA GUILLERMO PRÁCTICA

def join_files(file1,file2,file3):
    with open(file1,'r') as f1, open(file2,'r') as f2, open(file3,'a') as f3:
        f3.write(f1.read()+f2.read())

# Ejercicio 9
# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

def frecuencia_palabra(archivo):
    diccionario = {} # Creamos un diccionario vacío donde almacenaremos las palabras y su frecuencia
    palabras = 0 # Inicializamos el contador de palabras
    with open(archivo,'r') as file: # Abrimos el archivo en modo lectura
        for line in file: # Recorremos el archivo línea por línea
            linea = line.split() # Separamos cada línea en una lista de palabras
            for palabra in linea: # Recorremos la lista de palabras de cada línea
                palabras += 1 # Incrementamos el contador de palabras
                if palabra not in diccionario: # Si la palabra no está en el diccionario, la agregamos con una frecuencia de 1/palabras
                    diccionario[palabra] = 1/palabras
                else: # Si la palabra ya está en el diccionario, sumamos 1/palabras a su frecuencia
                    diccionario[palabra] += 1/palabras
        print(diccionario) # Imprimimos el diccionario con las palabras y sus frecuencias


# frecuencia_palabra('fi_ucema_burgos/practicas/texto_prueba.txt')


# Ejercicio 10
# Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.
import os

def concatenar_archivos_txt(carpeta):
    # Definimos la ruta de la carpeta de entrada y salida
    carpeta_entrada = os.path.join(carpeta, 'Carpeta1')
    carpeta_salida = os.path.join(carpeta_entrada, 'Resultado')
    
    # Si la carpeta de salida no existe, la creamos
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
    
    # Recorremos todos los archivos de la carpeta de entrada
    for archivo in os.listdir(carpeta_entrada):
        # Si el archivo es un .txt lo procesamos
        if archivo.endswith('.txt'):
            # Abrimos el archivo de entrada
            with open(os.path.join(carpeta_entrada, archivo), 'r') as file:
                # Leemos el contenido del archivo
                contenido = file.read()
                
                # Abrimos el archivo de salida en modo append
                with open(os.path.join(carpeta_salida, 'resultado.txt'), 'a') as out_file:
                    # Escribimos el contenido del archivo en el archivo de salida
                    out_file.write(contenido)

#falta mkdir y chdir


#10)Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.
ruta_carpeta1 = "C:/Users/fgige/Desktop/fi_ucema/practicas/carpeta 1" 
ruta_resultado = os.path.join(ruta_carpeta1, "resultado")       ## Definimos la ruta de la carpeta Carpeta1 y la carpeta Resultado
ruta_archivo_resultado = os.path.join(ruta_resultado, "resultado.txt")  # Definimos la ruta del archivo donde se van a concatenar los archivos .txt

archivo_resultado = open(ruta_archivo_resultado, "a") # Abrimos el archivo en modo "a" para añadir contenido al final del archivo si existe

for archivo in os.listdir(ruta_carpeta1): #recorremos todos los archivos de la carpeta
    if archivo.endswith(".txt"): #comprobamos que el archivo termine en txt
        ruta_archivo = os.path.join(ruta_carpeta1, archivo)
        archivo_txt = open(ruta_archivo, "r")

        contenido = archivo_txt.read()
        archivo_resultado.write(contenido)


def reemplazar(entrada, salida, letra):
    with open(salida, "a") as archivo1:
        with open(entrada, "r") as archivo2:
            texto = archivo2.read()
            texto2 = texto.replace(letra, letra + "\n")
            archivo1.write(texto2)