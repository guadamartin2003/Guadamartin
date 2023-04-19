from aves import pepita, anastasia, roberta

#pepita sabe volar porque lo hace sin quejarse
#print(pepita.volar_en_circulos())
#pepita no sabe hablar, además aprendimos que pepita es una Golondrina
#print(pepita.hablar())
#A pepita le gusta comer alpiste
#
# print(pepita.comer_alpiste(200))
"""
Sabemos que pepita es un objeto individual/único (instancia), 
en particular es un objeto de la clase Golondrinas
Que entiende mensajes (lo que las golondrinas entienden) 
y que tiene las características de una Golondría (atributos)
"""
print("Pepita al comienzo:", pepita.energia)
pepita.volar_en_circulos()
print("después de volar: ",pepita.energia)
pepita.comer_alpiste(200)
print("después de comer: ",pepita.energia)
print("hasta acá Pepita..")

"""Pepita tiene una energía basal. 
Ahora sabemos que pepita cuando le damos órdenes, está haciendo algo.
Y algo en su estado cambia(la energía).
- Entonces ahora sabemos que el estado de pepita está dado por su energía
- Pepita tiene como atributos o características saber volar y comer alpiste
- El estado de los objetos de alguna forma puede cambiar o modificarse
"""

print("En el caso de anastasia tiene de energía: ", anastasia.energia)
print(anastasia)
anastasia.volar_en_circulos()
print(anastasia.energia)
anastasia.comer_alpiste(200)
print(anastasia.energia)
""" Aprendimos que los objetos pueden tener distintos estados basales,uno propio cada uno
Aún con distintos estados, los objetos pueden entender los mismo mensajes (los mensajes se llaman métodos)
"""


print("LLamemos a Roberta")
print("Roberta al comienzo tiene de energía:", roberta.energia)
roberta.volar_en_circulos()
print("Energia despues de volar:", roberta.energia)
#roberta.comer_alpiste(200)
#print("Energia despues de comer alpiste:", roberta.energia)
#ups!Roberta es un dragón no come alpiste
roberta.escupir_fuego()
print("Energia despues de sacar fuego:", roberta.energia)
roberta.comer_peces(200)
print("Energia despues de comer peces:", roberta.energia)

"""Aprendimos que hay objetos que entienden 
los mismos mensajes aunque no sean de la misma clase.
Esos mensajes se llaman interfaz(el conjunto de mensajes que entienden).
"""

## Teoria
"""Los objetos no sabes si son o no polimórfico.
Los objetos que comparten su interfaz son polimorficos. 
En este caso vemos un polimorfismo parcial.
Para ver polimorfismo necesitamos un observador u otro actor.
"""