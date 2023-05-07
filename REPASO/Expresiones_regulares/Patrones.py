'[a-zA-Z0-9]'  #al menos un carácter permitido.
 #Explicación del patron: rangos de a-z, A-Z, 0-9 
 
'^[a-zA-Z0-9]*$'  #todo el string cumple con los caracteres permitidos
#Explicación del patron
# ^: El símbolo "^" indica que la búsqueda debe comenzar al inicio de la cadena.
# [a-zA-Z0-9]: Este conjunto de caracteres representa todos los caracteres permitidos en la cadena, que son letras minúsculas y mayúsculas y dígitos numéricos.
# *: El símbolo "*" indica que el conjunto de caracteres anterior puede estar presente cero o más veces.
# $: El símbolo "$" indica que la búsqueda debe terminar al final de la cadena.

'he*'  #tiene una h seguida de ninguna o más e.

'he+' #+ <-- al menos 1 "e" y ninguna otra letra

'he?' # ? <-- indica que la 'e' puede estar presente o no. Es decir, 0 o 1 vez

'he{2,3}' # {2,3} <-- Refiere al rango de veces que debe aparecer la 'e' Entre 2 y 3 veces.

'[a-zA-Z]+_+[a-zA-Z]+$'  #una palabra unida a otra con un guión bajo
# [a-zA-Z]+ <-- busca una o mas letras (primer palabra)
# _+ <-- busca uno o mas guiones 
# [a-zA-Z]+ <-- busca una o mas letras (segunda palabra)
# $ <-- Este símbolo indica el final de la línea.

'^'+str(numero) #si un string empieza con un número específico.
# ^ <-- REFIERE AL INICIO DEL STRING.

'\b{palabra}\b' # donde '\b' indica que se debe buscar la palabra completa y no como parte de otra palabra.

'[a-zA-Z0-9\s]+$'#contenga solamente letras minúsculas, mayúsculas, espacios y números.
 # [a-zA-Z0-9\s]+ <-- representa uno o más caracteres que pueden ser una letra (mayúscula o minúscula) o un número o un espacio en blanco.
 # $ <-- Representa el final del string.

'\d'  # <-- refiere a caracteres numéricos.

r'-(.*?)-' #extraiga los caracteres que estén entre guiones
# r <-- refiere a que la cadena es un raw string (los caracteres se toman como tal y no como metacaracteres Ej: \n --> \ n y no como salto de linea)
# - <-- el patrón comienza y termina con un guion
# (.*?) <-- es un grupo de captura que coincide con cualquier número de caracteres

'[@|&](.*?)[@|&]'#las substrings están delimitadas por los caracteres @ o &.
# Utilizamos la función re.findall() para buscar todas las ocurrencias del patrón "@(cualquier cosa)@" o "&(cualquier cosa)&"
    # En este caso, utilizamos la sintaxis '[@|&]' para indicar que puede ser cualquiera de estos dos caracteres
    # Utilizamos los paréntesis para indicar que sólo queremos extraer la subcadena que está entre los símbolos @ o &
    # El modificador ? se utiliza para que la búsqueda sea no-greedy, es decir, que la expresión regular trate de hacer el menor match posible
    # Si no utilizamos el modificador ?, la expresión regular buscará el match más grande posible, lo cual puede llevar a resultados inesperados

"(P\w*)\W(P\w*)" #verifique que dos palabras dentro del string empiecen con la letra P 
# EXPLICACIÓN DEL PATRÓN
# (P\w*) <-- Primer bloque. Refiere a primer palabra.
#\w <-- caracters alfanumericos o _ [a-zA-Z0-9_]
# \W <-- separador palabras. Negación \w [^a-zA-Z0-9_] <-- ^ dentro del rango actua como negación, no para referirse al incio.
# (P\w*) <-- Segundo bloque. Refiere a segunda palabra.

'^\w+[.-]?\w*@[a-zA-Z]+[.][a-z]+[.]?[a-z]?$'
# EXPLICACIÓN PATRÓN:
# ^\w+[.-]?\w* --> inicia con 1 o mas caracteres alfanumericos, que pueden estar seguidos o no de u '.' o '-', a lo que le pueden seguir o no otros caracteres alfanumércios .
# @ <-- le debe seguir una @ obligatoriamente
# [a-zA-Z]+[.][a-z]+ <-- a continuacion el dominio (incluye solo letras minusculas ej: 'gmail'). Luego separa un '.' obligatoriamente del 'com' o 'edu'
# [.]?[a-z]? <-- puede incluir el '.ar' por ejemplo. NO es necesacrio que lo incluya
# $ --> Fin de string. Incluir si o si si incluyo el ^ al inicio para 

"""
^ - Indica que la búsqueda debe comenzar desde el inicio de la cadena
\w+ - Indica que hay uno o más caracteres alfanuméricos al principio del mail
[.-]? - Indica que se puede tener opcionalmente un punto o un guion
\w* - Indica que hay cero o más caracteres alfanuméricos después del punto o guion
@ - Indica que debe aparecer una arroba
[a-zA-Z]+ - Indica que debe haber una o más letras después de la arroba
[.] - Indica que debe haber un punto
[a-z]+ - Indica que debe haber una o más letras minúsculas después del punto
[.]? - Indica que el último punto puede estar o no presente
[a-z]? - Indica que el último carácter puede ser una letra minúscula o no
"""