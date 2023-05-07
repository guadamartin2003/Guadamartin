class EntrenadorPokemon():
    def __init__(self, batallas_ganadas = 0, lista_pokemons = []):      # Porque = 0 o lista vacio. Por defecto, el valor de esos parametros es ese.
        self.batallas_ganadas = batallas_ganadas                        # Si no se le pasa ningun valor valen eso, si no, otros 
        self.pokemons = lista_pokemons

    def get_batallas_ganadas(self):
        return self.batallas_ganadas

    def get_pokemons(self):
        return self.pokemons

# c) Definir el método agregar_pokemon que incorpora un pokemon a la lista de pokemons que tiene un EntrenadorPokemon en su equipo.
    
    def agregar_pokemon(self, nuevo_pok):
        self.pokemons.append(nuevo_pok)

# d) Definir un método perder_batalla que descuenta 1 de las batallas_ganadas y elimina un pokemon de la lista de pokemons.

    def perder_batalla(self):
        self.pokemons.remove(self.pokemons[-1])     #elimina al ultimo
        self.batallas_ganadas -= 1 
    
    def perder_batalla2(self, nuevo_pok):
        self.pokemons.remove(nuevo_pok)     #elimina ese nuevo pok
        self.batallas_ganadas -= 1 

# a) ¿Cuál es el nombre de la clase? Entrenador Pokemon
#    ¿Cuál es el estado de un objeto de esta clase?  Estado (lista de atributos) --> self.batallas_ganadas y self.pokemons
#    ¿Qué mensajes entiende? Entiende (los metodos de la clase) cuando "le preguntas" que batallas ganó y la cantidad de pokemons que tiene


# b) Instanciá al EntrenadorPokemon Ash, que tiene 25 batallas_ganadas y a pikachu entre sus pokemons.

ash = EntrenadorPokemon(25, ['pikachu'])        # instanciar siempre en minuscula 

ash2 = EntrenadorPokemon()      # asi esta bien tambien 

print(ash.get_batallas_ganadas())
print(ash.get_pokemons())

ash.agregar_pokemon('pok')
print(ash.get_pokemons())

ash.perder_batalla()
print(ash.get_batallas_ganadas())
print(ash.get_pokemons())