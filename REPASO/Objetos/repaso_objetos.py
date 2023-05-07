#OBJETOS

class Cancion: # es la representacion de un objeto
  def __init__(self, un_titulo, una_banda): # self es la referencia al propio objeto o instancia particular
    self.titulo = un_titulo
    self.banda = una_banda

# El objeto es una instancia de una clase, es decir, una entidad que tiene un conjunto de atributos que la definen.
# El estado se refiere al valor de los atributos en un momento dado.
#Por ejemplo, si tenemos una clase "Perro" con atributos "nombre", "raza" y "edad", 
#podemos crear un objeto "mi_perro" con valores para cada uno de los atributos, 
#como "nombre='Max'", "raza='Labrador'" y "edad=3". 
# En este caso, el objeto "mi_perro" es una instancia de la clase "Perro" y su estado sería "nombre='Max'", "raza='Labrador'" y "edad=3".

#Cuando tiene un () se esta invocando una funcion
# cargar_a_tope() es una función que se ha definido para la clase celular_de_eli que carga completamente la batería del celular.
>>>celular_de_eli.cargar_a_tope()
>>>celular_de_eli.tiene_bateria_maxima()
True
>>>batman.necesita_descanso()
True
>>>superman.necesita_descanso()
False

#Para conocer el estado de un objeto, podemos acceder a cada uno de sus atributos escribiendo objeto.atributo,
# habrás notado que, a diferencia de cuando envíamos un mensaje, al acceder a un atributo no vamos a usar paréntesis.
>>>celular_de_eli.bateria
50
>>>celular_de_eli.saldo
300

#objeto#
pipita= "Golondrina" #: instancia

#diferencia entre metodo y funcion
#        los metodos se encuentran dentro de una clase y una funcion no
#diferencia entre metodo y procedimiento
#        la misma que la anterior

#los metodos estan siempre dentro de una clase podrian retornar algo los procedimientos no

#los objetos que comparten ciertos mensajes se llaman objetos polimorficos
    #tiene que haber un tercer mensaje


celular_de_lu=Celular(50,80)

class Celular:
  def __init__(self, una_bateria, un_saldo, un_sistema_operativo): #__init__ #es el constructor, define el estado inicial.
    self.bateria = una_bateria
    self.saldo = un_saldo
    self.sistema_operativo=un_sistema_operativo

  def tiene_bateria_maxima(self): #cargar a tope cambia mi bateria inicial a 100
    return self.bateria == 100
  # algunos metodos retornan otros no
  
  def cargar_a_tope(self):  #cargar a tope cambia mi bateria inicial a 100
    self.bateria=100
  #este no retorna nada
   
  def necesita_saldo(self): #retorna un booleano
    return self.saldo==0
  
class Gato:
  def __init__(self, una_energia, una_edad):
    self.energia=una_energia
    self.edad=una_edad

  def comer(self,gramos): # en esta funcion necesito que me digan los gramos para cambiar mi energia
    self.energia+=gramos

  def cumplir_anios(self):
    self.edad+=1

#objeto    #instancia    
mi_gato = Gato(10, 2)
print("Mi gato tiene", mi_gato.edad, "años y", mi_gato.energia, "gramos de comida en su estómago")

gato1 = Gato(10, 2) #inicial
print(gato1.edad)  # salida: 2
gato1.cumplir_anios()
print(gato1.edad)  # salida: 3


class EstudianteDeVeterinaria:
  
  def alimentar(self, animal, gramos):
    animal.comer(gramos)

  def rehabilitar(self, animal):
    animal.recibir_rehabilitacion()

  def puede_dar_el_alta(self, animal):
    return animal.esta_feliz()

class Gato:
  def __init__(self, energia, edad): #recibo esta informacion
    self.energia = energia
    self.edad = edad

  def comer(self, gramos):
    self.energia += gramos

  def esta_feliz(self):
    return self.energia > 30

  def recibir_rehabilitacion(self):
    self.comer(400)


class Caballo:
  def __init__(self, una_energia, una_raza, kms):
    self.energia = una_energia
    self.raza = una_raza
    self.kms = kms

  def comer(self, gramos):
    self.energia += gramos * 2 #modifica la energia

  def esta_feliz(self):
    return True

  def galopar(self, kms):
    self.energia -= kms #modifica la energia

  def kilometros_recorridos(self, kms):
     self.kms += kms


  def recibir_rehabilitacion(self):
    self.galopar(3)
    self.comer(3000)
    self.galopar(5)


class Golondrina:
  def __init__(self, una_energia, una_ciudad):
    self.energia = una_energia
    self.ciudad = una_ciudad

  def comer(self, gramos):
    self.energia += gramos / 2

  def esta_feliz(self):
    return self.ciudad == "Lihuel Calel"

  def volar_hacia(self, destino):
    self.ciudad = destino
    self.energia /= 2

  def recibir_rehabilitacion(self):
    self.volar_hacia("Lihuel Calel")

class Pasta:
    def __init__(self): #siempre inicio con 0 ajies
        self.ajies = 0
        # self solo porque ajies no cambia, cambia la cantidad
    def suavizar(self): 
      self.ajies -=1
      # self porque ajies no cambia, cambia la cantidad

class Pizza:
    def __init__(self):
        self.condimento = "adobo"
        # self porque el condimento no cambia siempre es el mismo
        
    def suavizar (self):
      self.condimento = "oregano"
      
class Chef:
    def __init__(self, plato_del_dia):
        self.plato_del_dia = plato_del_dia
    
    def picantear(self):
        if isinstance(self.plato_del_dia, Pasta):
          #La función isinstance(obj, clase) es una función incorporada de Python que se utiliza para verificar si un objeto (obj) es una instancia de una clase determinada (clase). 
          # En el código proporcionado, se utiliza la función isinstance para verificar si self.plato_del_dia es una instancia de la clase Pasta o Pizza. 
          # Dependiendo de la instancia, se realizan diferentes acciones en el método picantear del objeto Chef. 
          # En resumen, isinstance es una función que ayuda a determinar si un objeto es de un determinado tipo de clase.
            if self.plato_del_dia.ajies > 10:
                raise Exception("El plato ya está demasiado picante")
            else:
                self.plato_del_dia.ajies += 5
        elif isinstance(self.plato_del_dia, Pizza):
            if self.plato_del_dia.condimento == "cayena":
                raise Exception("El plato ya está demasiado picante")
            else:
                self.plato_del_dia.condimento = "cayena"
        else:
            raise Exception("El chef solo puede picantear pastas o pizzas")

class AyudanteDeCocina:
    def suavizar(self, plato):
       plato.suavizar()

class Notebook:
    def __init__(self, bateria):
        self.bateria = bateria

    def utilizar(self, minutos):
        self.bateria -= minutos #minutos cambia mi nivel de bateria
    # no inicializo con minuto porque inicializo con bateria y los minutos cambian la bateria
    
    def tiene_bateria(self):
        return self.bateria > 20

    def tiene_bateria_maxima(self):
        return self.bateria == 100

    def cargar_a_tope(self):
        self.bateria = 100

class Dispositivo:
    def __init__(self, bateria):
        self.bateria = bateria
        
    def tiene_bateria(self):
        return self.bateria > 20

    def tiene_bateria_maxima(self):
        return self.bateria == 100

    def cargar_a_tope(self):
        self.bateria = 100

class Tablet(Dispositivo):

    def utilizar(self, minutos):
        self.bateria -= minutos / 2

class Notebook(Dispositivo):

    def utilizar(self, minutos):
        self.bateria -= minutos


Dispositivo es una clase concreta.


Dispositivo es una clase abstracta. correcta


Tablet es una clase concreta. correcta


Tablet es una clase abstracta.


Notebook es una clase concreta. correcta


Notebook es una clase abstracta.


Tablet hereda de Dispositivo. correcta


Dispositivo hereda de Tablet.


Notebook hereda de Dispositivo. correcta


Dispositivo hereda de Notebook. 


Las clases abstractas proveen comportamiento a sus subclases. correcta


Las clases abstractas se utilizan para crear instancias.


Las clases concretas proveen comportamiento a su superclase.


Las clases concretas se utilizan para crear instancias. correcta

class MedioDeTransporte:
    def __init__(self, combustible):
        self.combustible = combustible

    def cargar_combustible(self, cantidad):
        self.combustible += cantidad
        #modifica el combustible del innit

    def entran_personas(self, cantidad):
        return cantidad <= self.maximo_personas()

class Moto(MedioDeTransporte):
    def maximo_personas (self):
      return 2

    def recorrer(self, kilometros):
        self.combustible -= kilometros

class Auto(MedioDeTransporte):
    def maximo_personas(self):
      return 5

    def recorrer(self, kilometros):
        self.combustible -= kilometros/2

class Colectivo(MedioDeTransporte):
    maximo_personas = None

    def __init__(self):
        self.combustible = 100
        self.pasajeros = 0

    def entran_personas(self, cantidad):
        return True

class Libro:
    def __init__(self, titulo, paginas, genero, autoria):
        self.titulo = titulo
        self.paginas = paginas
        self.genero = genero
        self.autoria = autoria
    
    def es_largo(self):
        return self.paginas > 300
    
    def nacionalidad(self):
        return self.autoria["nacionalidad"]

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def libros_largos(self):
        return [libro for libro in self.libros if libro.es_largo()]
    
    def titulos_disponibles(self):
        return [libro.titulo for libro in self.libros]

#Ejercicio 7
#Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como
#CSS (coeficiente de serenidad silenciosa), 
#CSSP y CSSV (como el CSS pero “pico” y “veces”). 
#El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, 
#por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división 
#pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió. 
#El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió,
#los coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.

class Gorrion:
   
   def __init__(self):
        self.kilometros = []
        self.gramos = []


