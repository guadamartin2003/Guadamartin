"""
En un mundo distópico la humanidad es atacada sin descanso por titanes. 
Estos titanes son muy resistentes pero no inmortales, su salud (100 de máxima) puede ir disminuyendo si reciben daño 
debido a algún ataque, y si llega a 0 se muere. Al recibir este ataque la salud disminuye 1.5 por cada puntos de daño recibido. 
Además tienen la capacidad de destruir cierto número de casas dependiendo de su salud, siendo 8 casas cuando su salud es máxima 
o un número proporcional si su salud es menor a la máxima 
(si tiene 60 puntos de salud destruiría 4.8 casas, es decir, 4 casas completas y más de la mitad de otra). 
Sin embargo no tienen la capacidad de comunicarse con los humanos, siendo un grito, "¡Aaaarrrg!", el único sonido que hacen.
Definí la clase Titan con los atributos y métodos correspondientes. Además instanciá a un Titan y ejecutá las siguientes líneas:

titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
titan1.destruir_casas()
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())
cuyo resultado tiene que ser:

True
55
4.4
"¡Aaaarrrg!"
5.0
False
"""
class Titan():
	def __init__(self, salud):
		self.salud = salud
		self.correr = False

	def salud_actual(self):
		return self.salud

	def recibir_ataque(self, cantidad):
		self.salud -= 1.5 * cantidad

	def grito(self):
		return "¡Aaaarrrg!"

	def cuantas_casas(self):
		return (self.salud * 8 / 100)

	def destruir_casas(self):
		if (self.cuantas_casas() > 1):
			if ((self.cuantas_casas() % 1) > 0):
				self.salud -= (self.cuantas_casas() // 1) * 12.5
			else:
				self.salud -= (self.cuantas_casas() - 1) * 12.5
		else:
			print("No puede destruir ninguna casa")

	def esta_vivo(self):
		return (self.salud > 0)



titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
titan1.destruir_casas()
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())
"""
Se está pensando en el diseño de un juego que incluye la nave espacial Enterprise. En el juego, esta nave tiene un nivel de potencia de 0 a 100, y un nivel de coraza de 0 a 20. La Enterprise puede:

encontrarse con una pila atómica, en cuyo caso su potencia aumenta en 25.
encontrarse con un escudo, en cuyo caso su nivel de coraza aumenta en 10.
recibir un ataque, en este caso se especifican los puntos de fuerza del ataque recibido. La Enterprise "detiene" el ataque con la coraza, y si la coraza no alcanza, el resto se descuenta de la potencia. Por ejemplo si la Enterprise con 80 de potencia y 12 de coraza recibe un ataque de 20 puntos de fuerza, puede parar solamente 12 con la coraza, los otros 8 se descuentan de la potencia. La nave debe quedar con 72 de potencia y 0 de coraza. Si la Enterprise no tiene nada de coraza al momento de recibir el ataque, entonces todos los puntos de fuerza del ataque se descuentan de la potencia.
La potencia y la coraza tienen que mantenerse en los rangos indicados, por ejemplo, si la Enterprise tien 16 puntos de coraza y se encuentra con un escudo, entonces queda en 20 puntos de coraza, no en 26. Tampoco puede quedar negativa la potencia, a lo sumo queda en 0. La Enterprise nace con 50 de potencia y 5 de coraza. Implementar este modelo de la Enterprise, que tiene que entender los siguientes mensajes:

potencia()

coraza()

encontrarPilaAtomica()

encontrarEscudo()

recibirAtaque(puntos)

Al ejecutar esto:

enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
la potencia de la Enterprise debe ser 66, y su coraza debe ser 10.

Agregar al modelo de la Enterprise, la capacidad de entender estos mensajes.

fortalezaDefensiva(), que es el máximo nivel de ataque que puede resistir, o sea, coraza más potencia.
necesitaFortalecerse(), tiene que ser true si su coraza es 0 y su potencia es menos de 20.
fortalezaOfensiva(), que corresponde a cuántos puntos de fuerza tendría un ataque de la Enterprise. Se calcula así: si tiene menos de 20 puntos de potencia entonces es 0, si no es (puntos de potencia - 20) / 2.

"""
class Enterprise():
	def __init__(self):
		self.potencia = 50
		self.coraza = 5

	def potencia_actual(self):
		return self.potencia

	def coraza_actual(self):
		return self.coraza

	def encontrarPilaAtomica(self):
		if self.potencia + 25 <= 100:
			self.potencia += 25
		else:
			self.potencia = 100

	def encontrarEscudo(self):
		if self.coraza + 10 <= 20:
			self.coraza += 10
		else:
			self.coraza = 20

	def recibirAtaque(self, puntos):
		if puntos <= self.coraza:
			self.coraza -= puntos
		else:
			self.potencia -= puntos - self.coraza
			self.coraza = 0

	def fortalezaDefensiva(self):
		return (self.coraza + self.potencia)

	def necesitaFortalecerse(self):
		return (self.coraza == 0 and self.potencia < 20)
		
	def fortalezaOfensiva(self):
		if self.potencia >= 20:
			return ((self.potencia - 20) / 2)
		else:
			return 0

enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
# la potencia de la Enterprise debe ser 66, y su coraza debe ser 10.

"""
Los estudiantes (como ustedes) son como cualquier persona, las cuales recuperan energía si duermen o si comen, o la gastan al hacer ejercicio, sin embargo en particular los estudiantes también gastan energía al estudiar y se sienten felices al aprobar algún exámen. Resumiendo, las personan pueden:

Decirnos cuánta energía tienen.
Recuperar el máximo de energía (100) al dormir 8 horas, o el proporcional si duermen menos (si duermen 4 ganan la mitad de energía, es decir 50).
Recuperar energía al comer, ganando de esta manera 10 puntos.
Gastar energía al hacer ejercicio, siendo un gasto de 25 puntos por cada media hora de ejercicio.
Como estado de ánimo pueden estar felices o no, pero por defecto no están felices.
Además los estudiantes tienen el siguiente comportamiento:

Al estudiar su energía disminuye 20 puntos por cada hora de estudio.
Si aprueban su estado de ánimo pasa a ser "Feliz".
Definí las clases Persona y Estudiante con los atributos y métodos correspondientes y hacé que esta última herede de la primera. Además instanciá a un Estudiante y ejecutá las siguientes líneas:

"""
class Persona:
    def __init__(self, energia):
        self.energia = energia
        self.feliz = False

    def obtener_energia(self):
        return self.energia

    def dormir(self, horas):
        self.energia += horas * 12.5  # Se recupera 12.5 puntos de energía por hora de sueño

    def comer(self):
        self.energia += 10

    def hacer_ejercicio(self, minutos):
        self.energia -= minutos * 0.8333  # Se gasta 0.8333 puntos de energía por minuto de ejercicio

    def estado_animo(self):
        return self.feliz


class Estudiante(Persona):
    def estudiar(self, horas):
        self.energia -= horas * 20

    def aprobar(self):
        self.feliz = True
        return self.feliz

    def energia_actual(self):
        return self.energia


estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
estudiante.aprobar()
print(estudiante.aprobar())
print(estudiante.energia_actual())


