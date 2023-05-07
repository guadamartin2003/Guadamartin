# Obtener la lista de subsecuencias delimitadas por 'X' e 'Y', que incluyan la subsecuencia 'ab'.
# Por ejemplo para XbaaaYjXababYqXbabbbbaaYqXffeeY, hay que devolver ['abab', 'babbbaa'].

import re

patron = "X(.*?ab.*?)Y" #signo de preg favorecer matches internos

patron_ok = "X([^X]*?ab[^Y].*?)Y"

def funcion1(string):
    print(re.findall(patron_ok, string))

funcion1("XbaaaYjXababYqXbabbbbaaYqXffeeY")

# . cualquier carac 
# * 0 o mas veces
# ? matches internos --> que mire adentro y no solo los bordes
#.*? Coincide con cualquier número (incluido cero) de caracteres, de manera no codiciosa.
#También utiliza el modificador ? no codicioso para que coincida con la subsecuencia más corta posible.


# Onomatopopih está aprendiendo expresiones regulares y le pidieron construir una función que sea capaz de extraer
# la lista de substrings delimitadas por los patrones 'ag' y 'cta', no incluyan números.
# Revisá su código propuesto y marcá con una `x` las opciones correctas. JUSTIFICA tus respuestas.

import re

def funcionDeExpresiones_Regulares(string):
    print(re.findall("ag(\d.*?)cta", string))

funcionDeExpresiones_Regulares('aabocaggaaactazu4lggaasag24gra1ndecta')


'''

  - El nombre de la función de Onomatopopih respeta las convenciones de nombres de Python.
    NO, las convenciones dicen que las funciones tienen que estar en separadas por un _ en minus.
X - La función devuelve NameError al ser ejecutada. VERDADERO.
        Previo al codigo de de la funcion, hay que llamar a la biblioteca RE con un import re
  - La función devuelve SintaxError al ser ejecutada
  - Una vez corregida la función, cuando se la invoca usando el texto 'aabocaggaaactazu4lggaasag24gra1ndecta' devuelve ['gaaa']

X - Una vez corregida la función, cuando se la invoca usando el texto 'aabocaggaaactazu4lggaasag24gra1ndecta' devuelve ['24gra1nde']
    Falso, si se corrige la funcion agregando un print para que devuelva el resultado ['24gra1nde'].

# Findal --> Atribuite Error

'''

def entre_ag_y_cta_sin_numeros2(string):
    print(re.findall("ag([^\d]*)cta", string))

entre_ag_y_cta_sin_numeros2('aabocaggaaactazu4lggaasag24gra1ndecta')