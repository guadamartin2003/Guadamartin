# Escribir funciones que, dado un String, permitan responder lo siguiente:

# a) obtener la lista de los substrings delimitados entre '<' y '>' que no incluyan ninguna 'o'.

import re

def delimitados_piquitos_sin_o(string):
    print(re.findall("<([^o].*?)>", string))

#El corchete [] se utiliza para definir una clase de caracteres, y 
#el símbolo ^ dentro de la clase se utiliza como negación, 
# lo que significa que coincide con cualquier carácter que no esté dentro de la clase especificada.

delimitados_piquitos_sin_o("ds<hola>hsb<hhj>sdk<469>nkd")

# b) Onomatopopih, que aún no sabe mucho de expresiones regulares,
# nos mandó una función que debería ser capaz de decirnos si un string incluye o no un substring de 3 letras,
# cada una de las cuales debe ser a, b ó c. Esto es, alcanza con incluir, p.ej, 'abc', 'cbc', 'aac', 'ccc'.

# En base a la función que definió respondé:

# ¿Qué error/es tiene? (justificando la respuesta).
# Uno de los errores esta en el patron, el metacaracter {3} solo influye en la c; y tampoco da lugar a que haya match con las 3 letras en otro orden
# Tendria que usar re.search para que la funcion nos diga SI INCLUYE O NO el substring. Con el findall, si la funcion esta escrita correctamente, devolvera la lista de coincidencias. 

# Modificá la función para que cumpla lo requerido correctamente.

def triples(string):
    return re.findall("abc{3}", string)

triples("svsslkvabckjsv")


def triples_correcta(string):
    print(bool(re.search("[a-c]{3}", string)))

# probando 
triples_correcta("svsslkvkjabcuhjv")
triples_correcta("svsslkvkjbbcuhjv")
triples_correcta("svsslkvkjabuhjv")
triples_correcta("svssalkvbkjcuhjv")