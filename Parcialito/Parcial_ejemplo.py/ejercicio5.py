# Los árboles de casi todas las especies se comportan de manera similar, casi sin importar las condiciones de luz o climáticas.

# Se propone modelar este comportamiento en una clase, sabiendo que los árboles tienen como principal característica
# si son perennes (no pierden las hojas), una cantidad de agua, nutrientes y altura.

class Arbol:
    
    def __init__(self, agua = 0, nutrientes = [], altura = 0):
        self.agua = agua
        self.nutrientes = nutrientes
        self.altura = altura
        self.son_perennes = True 

    def hacer_fotosistesis(self, tiempo):
        self.nutrientes = self.nutrientes +  (1 * (tiempo/10))
    
    def absorber_agua(self, cantidad):
        self.agua +=cantidad
    
    def crecer(self):
        if self.nutrientes == 100 and self.agua == 100:
            self.altura += 1

# hacer_fotosistesis(tiempo), la cual aumenta los nutrientes de la misma (1 punto cada 10 minutos),
# absorber_agua(cantidad), el cual aumenta el agua en cierta cantidad
# crecer(), en el cual, si se cumplen las condiciones de nutrientes y agua (100 puntos de cada uno),
# se aumenta la altura en 1 cm.

# El manzano tiene como característica un poco más particular,
# que genera frutos, las manzanas.

# Esto hace que la planta gaste energía en formar estos frutos,
# por lo que para crecer 1 cm necesita 150 puntos de agua
# y 200 de nutrientes.
# Además este árbol no es perenne.

class Manzano(Arbol):

    def __init__(self):
        self.son_perennes = False
    
    def crecer(self):
        if self.nutrientes == 200 and self.agua == 150:
            self.altura += 1

# Definí las clases Arbol y Manzano,
# hacé que esta último herede de la primera agregando y/o redefiniendo los métodos necesarios.