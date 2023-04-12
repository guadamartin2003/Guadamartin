#ejercicio 1

def caracteres_permitido(string):
    return bool(re.search('[a-zA-Z0-9.]', string))

#ejercicio 2

def caracteres_permitidos(string):
    return not bool (re.search('[^a-zA-Z0-9]', string))

#ejercicio 3

import re

def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro parton"
    
    # * 0 vos veces

def encontrar_patron(string):
    patron = "he?"
    if re.search(patron, string) is not None:
        return "se encontro el patron"
    else:
        return "No se encontro el patron"
    
def encontrar_patron(string):
    patron = "he{2,3}"
    if re.search(patron, string) is not None:
        return "se encontro el patron"
    else:
        return "No se encontro el patron"
    
# Ejercicio 4
def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "Patron encontrado"
    else:
        return "Patron encontrado"
    
