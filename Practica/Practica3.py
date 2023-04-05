# Pedimos al usuario que ingrese la letra a buscar
letra = input("Ingrese la letra a buscar al principio de las líneas: ")

# Abrimos el archivo en modo lectura
with open("archivo.txt", "r") as archivo:
    # Inicializamos un contador para las líneas que no empiezan con la letra buscada
    lineas_sin_letra = 0
    
    # Recorremos todas las líneas del archivo
    for linea in archivo:
        # Si la línea no comienza con la letra buscada, incrementamos el contador
        if not linea.startswith(letra):
            lineas_sin_letra += 1
    
    # Imprimimos el resultado
    print("El archivo tiene", lineas_sin_letra, "líneas que no empiezan con la letra", letra)
