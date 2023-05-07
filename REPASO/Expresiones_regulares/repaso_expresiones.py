
import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.match(patron, texto)) # solo le importa si la primera palabra coincide con el patron

import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.search(patron, texto)) #search busca la primera coincidencia con el patron y devuelve la posicion

import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.search(patron, texto).group()) #group() devuelve la cadena de texto que coincide con el patrón.

import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.findall(patron, texto)) # devuelve lista con todas las coincidencias

import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
re.search(patron, texto).group()
'amet'
re.search(patron, texto).group(0)
'amet'

#El método group() (o group(0)) nos devuelve la coincidencia. Sin embargo si lo que se quiere no es encontrar un patrón en particular, sino obtener lo que está dentro de cierto patrón (por ejemplo lo que hay entre ciertas palabras) hay que modificar el patrón. Vamos a ver el siguiente ejemplo:

import re
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*)sit"
re.search(patron, texto).group()
'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
re.search(patron, texto).group(0)
'ipsum dolor sit amet, consectetur ipsum elit. Amet sit'
re.search(patron, texto).group(1)
' dolor sit amet, consectetur ipsum elit. Amet '

import re
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*?)sit" #? una sola vez 
re.search(patron, texto).group()
'ipsum dolor sit'
re.search(patron, texto).group(0)
'ipsum dolor sit'
re.search(patron, texto).group(1) #solo lo del medio
' dolor  '

#Cuando se quieren obtener todas las apariciones del patrón se utiliza el método findall el cual actúa para cada coincidencia como si devolviera el group(1), es decir devuelve en una lista la parte que se encuentra dentro de los delimitadores.
import re
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*?)sit"
re.findall(patron, texto)
[' dolor ', ' elit. Amet ']

re.sub(patron, "###", texto) #La función sub permite reemplazar todos las ocurrencias del patrón por otro patrón en un String.