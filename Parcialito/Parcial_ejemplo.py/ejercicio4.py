# a) Onomatopopih está aprendiendo expresiones regulares y le pidieron construir una función que sea capaz de extraer un teléfono de
# 8 números que comienza con 4, a partir de un archivo base_de_telefonos.txt.

# Revisá su código propuesto y marcá con una [x] las opciones correctas.
# JUSTIFICA tus respuestas.


def extractorDeTel(path):
    with open(path, 'w') as miarch:
        texto = miarch.read()
        return re.match("4([0-9]{8})", texto)

# La función devuelve NameError al ser ejecutada.
# Va a dar NameError si no llamamos a la biblioteca RE!!

# La función devuelve SyntaxError al ser ejecutada

# [x] La función devuelve io.UnsupportedOperation al ser ejecutada. 
# Porque el archivo se abre en modo w (write) y en la siguiente linea el archivo se lee (con el modo .read())

# Cuando se invoca la función extractorDeTel usando el texto 'oahsdgfjhdgfjagdsfjsdgfkdgfks42948555' devuelve 4
# Cuando se invoca la función extractorDeTel usando el texto 'oahsdgfjhdgfjagdsfjsdgfkdgfks42948555' devuelve 42948555

# Las dos opciones de aca arriba, asi como esta dada la fucion, son incorrectas.
# El patrón no es el correcto para extraer un teléfono de 8 números que comienza con 4
# "^4[0-9]{7}" este patron podria funcionar, no llegue a porbarlo :(

# [x] Para compartir los cambios con sus compañeros Onomatopopih debe escribir git add . en la terminal y luego git commit -m "mi mensaje" y git push.
# CORRECTO Una vez que termino y guardó sus cambios, deberá realizar esos tres pasos, en ese orden, para actuzalizar el repositorio compartido. 
# Cabe aclarar que antes de realizar sus cambios y esa serie de pasos, debe hacer un git pull para descargar los aportes de sus compañeros, si es que se realizo alguno.

# Para compartir los cambios con sus compañeros Onomatopopih debe primero escribir git commit -m "mi mensaje" y git push

# Para descargarse los aportes de sus compañeros Onomatopopih debe escribir en la terminal git push
# [x] Para descargarse los aportes de sus compañeros Onomatopopih debe escribir en la terminal git pull.
# CORRECTO. Con el git pull descarga el aporte de sus compañeros 


