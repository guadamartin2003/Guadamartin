#Ejercicio 1
#Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
# Definimos un string de ejemplo
string_ejemplo = "Este es un string con algunos caracteres permitidos como a-z, A-Z y 0-9."

# Definimos una función que verifica si el string tiene caracteres permitidos
def tiene_caracteres_permitidos(string):
    # Definimos una lista de caracteres permitidos
    caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # Recorremos el string y comprobamos si cada carácter está en la lista de caracteres permitidos
    for caracter in string:
        if caracter in caracteres_permitidos:
            return True
    return False

# Llamamos a la función con el string de ejemplo e imprimimos el resultado
if tiene_caracteres_permitidos(string_ejemplo):
    print("El string tiene al menos un carácter permitido.")
else:
    print("El string no tiene ningún carácter permitido.")

#Ejercicio 2
#Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9
# Definimos un string de ejemplo
string_ejemplo = "Este es un string con algunos caracteres permitidos como a-z, A-Z y 0-9."

# Definimos una función que verifica si el string tiene todos sus caracteres permitidos
def tiene_todos_los_caracteres_permitidos(string):
    # Definimos una lista de caracteres permitidos
    caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # Recorremos el string y comprobamos si cada carácter está en la lista de caracteres permitidos
    for caracter in string:
        if caracter not in caracteres_permitidos:
            return False
    return True

# Llamamos a la función con el string de ejemplo e imprimimos el resultado
if tiene_todos_los_caracteres_permitidos(string_ejemplo):
    print("El string tiene todos sus caracteres permitidos.")
else:
    print("El string tiene al menos un carácter no permitido.")

#Ejercicio 3
#Creá un programa que verifique las siguientes condiciones:

#si un string dado tiene una h seguida de ninguna o más e.

#si un string dado tiene una h seguida de una o más e.

#si un string dado tiene una h seguida de una o más e.

#si un string dado tiene una h seguida de dos o tres e.

# Definimos un string de ejemplo
string_ejemplo = "hello world"

# Verificamos si el string tiene una h seguida de ninguna o más e
if "he" in string_ejemplo:
    print("El string tiene una h seguida de ninguna o más e.")

# Verificamos si el string tiene una h seguida de una o más e
if "hee" in string_ejemplo:
    print("El string tiene una h seguida de una o más e.")

# Verificamos si el string tiene una h seguida de dos o tres e
if "heee" in string_ejemplo or "heeee" in string_ejemplo:
    print("El string tiene una h seguida de dos o tres e.")

#Ejercicio 4
#Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).
# Definimos un string de ejemplo
string_ejemplo = "python_programming"

# Separamos el string por el guión bajo
palabras = string_ejemplo.split("_")

# Verificamos si hay dos palabras en la lista
if len(palabras) == 2:
    print("Se encontró la palabra", palabras[0], "unida a", palabras[1], "con un guión bajo.")
else:
    print("No se encontró ninguna palabra unida con un guión bajo.")

#Ejercicio 5
#Escribí un programa que diga si un string empieza con un número específico.

# Definimos el string y el número específico
string_ejemplo = "12345-abcdef"
numero_especifico = "123"

# Verificamos si el string empieza con el número específico
if string_ejemplo.startswith(numero_especifico):
    print("El string empieza con", numero_especifico)
else:
    print("El string no empieza con", numero_especifico)

#Ejercicio 6
#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada
# Definimos la frase y la lista de palabras a buscar
frase = "El perro come su comida en la casa"
palabras = ["perro", "gato", "comida", "agua"]

# Verificamos si las palabras están en la frase
for palabra in palabras:
    if palabra in frase:
        print("La palabra", palabra, "está en la frase.")
    else:
        print("La palabra", palabra, "no está en la frase.")

#Ejercicio 7
#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.
# Definimos el string a verificar
string_ejemplo = "Este es un string con números 123 y espacios"

# Verificamos si el string cumple con las condiciones
if string_ejemplo.isalnum() or " " in string_ejemplo:
    print("El string cumple con las condiciones.")
else:
    print("El string no cumple con las condiciones.")

#Ejercicio 8
#Escribí un programa que separe y devuelva los caracteres númericos de un string.
# Definimos el string de ejemplo
string_ejemplo = "abc123def456ghi789"

# Creamos una lista vacía para guardar los caracteres numéricos
caracteres_numericos = []

# Recorremos cada caracter del string
for caracter in string_ejemplo:
    # Si el caracter es un dígito, lo agregamos a la lista de caracteres numéricos
    if caracter.isdigit():
        caracteres_numericos.append(caracter)

# Imprimimos los caracteres numéricos encontrados
print("Los caracteres numéricos encontrados son:", "".join(caracteres_numericos))

#Ejercicio 9
#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
# Definimos el string de ejemplo
string_ejemplo = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"

# Creamos una lista vacía para guardar los caracteres entre guiones
caracteres_entre_guiones = []

# Separamos el string en palabras usando el método split()
palabras = string_ejemplo.split()

# Recorremos cada palabra del string
for palabra in palabras:
    # Si la palabra empieza con un guión y termina con un guión, agregamos los caracteres entre ellos a la lista
    if palabra.startswith("-") and palabra.endswith("-"):
        caracteres_entre_guiones.append(palabra[1:-1])

# Imprimimos los caracteres encontrados
print("Los caracteres entre guiones son:", ", ".join(caracteres_entre_guiones))

#Ejercicio 10
#Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &
import re

string = "Esta es una @substring@ y esta es otra &substring& dentro de una string"
pattern = r"[@&]\w+[@&]"
matches = re.findall(pattern, string)

for match in matches:
    print(f"Substring: {match}, Posición: {string.index(match)}")

#Ejercicio 11
#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
lista_strings = ["Práctica Python", "Práctica C++", "Práctica Fortran"]

for string in lista_strings:
    palabras = string.split()
    palabras_con_p = [palabra for palabra in palabras if palabra.startswith('P')]
    if len(palabras_con_p) >= 2:
        print(f"En el string '{string}' se encontraron las palabras {palabras_con_p[0]} y {palabras_con_p[1]} que empiezan con P.")

#Ejercicio 12
#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).
cadena = "Esta_es:una cadena con espacios, guiones_bajos y dos:puntos."
cadena_modificada = cadena.replace(" ", "|").replace("_", "|").replace(":", "|")
print(cadena_modificada)

#Ejercicio 13
#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

import re

cadena = "!Hola, ¿cómo estás? ¿Todo bien?"
patron = re.compile(r"[^a-zA-Z0-9]{2}")
cadena_modificada = patron.sub("__", cadena, count=2)
print(cadena_modificada)

#Ejercicio 14
#Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
texto = "Este es un    ejemplo con   muchos espacios    y     tabulaciones."
texto_reemplazado = texto.replace(" ", ";").replace("\t", ";")
print(texto_reemplazado)

#Ejercicio 15
#Realizá un programa que validar si una cuenta de mail está escrita correctamente.

import re

def validar_email(email):
    """
    Verifica si la dirección de correo electrónico es válida
    """
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, email)

# Ejemplo de uso
email = "usuario@example.com"
if validar_email(email):
    print("La dirección de correo electrónico es válida")
else:
    print("La dirección de correo electrónico no es válida")
