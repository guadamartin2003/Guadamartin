"""""
Ejercicio 1
Dadas las siguientes clases responder:

cuales son sus estados

cuales son sus interfaces

¿Comparten interfaz?

¿Son polimórficas?

Clase Perro:

Estados: Los estados de la clase Perro son alimento y caricias.
Interfaz: La interfaz de la clase Perro incluye los métodos energia, comer, alimento, acariciar, estaDebil y pasear.
No comparten interfaz con otras clases, ya que es una clase independiente.
No son polimórficas, ya que no heredan ni implementan la misma interfaz de otras clases.
Clase Gato:

Estados: Los estados de la clase Gato son alimento y caricias.
Interfaz: La interfaz de la clase Gato incluye los métodos energia, comer, caricias, acariciar y estaDebil.
No comparten interfaz con otras clases, ya que es una clase independiente.
No son polimórficas, ya que no heredan ni implementan la misma interfaz de otras clases.
En resumen, las clases Perro y Gato tienen diferentes estados y no comparten la misma interfaz. Además, no son polimórficas, ya que no heredan ni implementan la misma interfaz de otras clases.
"""


class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

    def alimento(self):
        print(self.alimento)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self.caricias < 2

    def pasear(self, km):
        self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

    def caricias(self):
        print(self.caricias)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self.caricias < 4
    

"""
Ejercicio 2
Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio. 
Este equilibrio se alcanza cuando la energía se encuentra entre 150 y 300.
"""
    
class Golondrina:
    def __init__(self, energia):
        self.energia = energia

    def volar(self, kms):
        self.energia -= 10 + 0.1 * kms

    def comer(self, gramos):
        self.energia += 4 * gramos

    def esta_en_equilibrio(self):
        return 150 <= self.energia <= 300

"""
Ejercicio 4
Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:

comienzan con una cantidad que podemos establecer de combustible

los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio litro de combustible por cada kilómetro recorrido

las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;

pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible

saben responder si entran una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera.
"""

class MedioDeTransporte:
    def __init__(self, combustible_inicial):
        self.combustible = combustible_inicial

    def cargar_combustible(self, cantidad):
        self.combustible += cantidad

    def hay_espacio(self, cantidad_personas):
        return cantidad_personas <= self.capacidad_maxima()

class Auto(MedioDeTransporte):
    def __init__(self, combustible_inicial):
        self.combustible = combustible_inicial
        self.capacidad_maxima = 5


    def consumir_combustible(self, distancia):
        consumo = distancia * 0.5
        if consumo <= self.combustible:
            self.combustible -= consumo
        else:
            print("No hay suficiente combustible para recorrer esa distancia")


class Moto(MedioDeTransporte):
    def __init__(self, combustible_inicial):
        self.combustible = combustible_inicial
        self.capacidad_maxima = 2

