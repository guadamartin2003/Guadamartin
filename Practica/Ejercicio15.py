#import re
#def mail_correcto(string):
 #   return bool(re.search('^\w+[.-]?\w*@[a-z]+[.][a-z]+[.]?][a-z]?'), string)
#print(mail_correcto('guadamartin@gmail.com'))
#print(mail_correcto('guada-martin@gmail.com'))

import re

def mail_correcto(string):
    return bool(re.search('^\w+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?', string))

print(mail_correcto('guadamartin@gmail.com'))

#polimorfismo
#estado: conjunto de atributos
#interfaz: 
#atributo: self.energia, self.edad
#parametro:lo que esta entre parentesis , self no es un parametro
