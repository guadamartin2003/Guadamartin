#como clonar un repo


#Pacman
class PacMan:
    def _init_(self):
        self.puntos = 0
        self.vidas = 3
        #velocidad opcional
    
    def comer_bolita(self, cantidad):
        self.puntos += (cantidad*2)
    
    def velocidad(self):
        return (2 + self.puntos)/100
    
    def perder_vida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print("Game over")
    
    def comer_fantasma(self, fantasma, color):
        self.puntos += fantasma.puntos_color(color)
class Fantasma:
    def _init_(self):
        self.fantasmas = {"rosa": 8, "verde": 6, "naranja": 4, "rojo": 2}
    
    def puntos_color(self, color):
        return self.fantasmas[color]
    


pacman = PacMan()
fantasma = Fantasma()


class PacMan:
    def _init_(self):
        self.puntos = 0
        self.vidas = 3
        #velocidad opcional
    
    def comer_bolita(self, cantidad):
        self.puntos += (cantidad*2)
    
    def velocidad(self):
        return (2*self.puntos)/100
    
    def perder_vida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print("Game over")
    
    def comer_fantasma(self, fantasma, color):
        fantasma.set_color(color)
        self.puntos += fantasma.puntos_color()

class Fantasma:
    def _init_(self):
        self.color = None

    def set_color(self, color):
        self.color =color
    
    def puntos_color(self):
        return self.color.puntos()
    

class Rojo:
    def puntos(self):
        return 2        

class Rosa:
    def puntos(self):
        return 4      

class Naranja:
    def puntos(self):
        return 6     

class Verde:
    def puntos(self):
        return 8     
    
pacman = PacMan()
rojo = Rojo()
rosa = Rosa()
naranja = Naranja()
verde = Verde()
fantasma = Fantasma()


#b) mejor forma de hacerlo

class PacManMejorado(PacMan):
    def vida_extra(self):
        if self.puntos >= 200:
            self.vidas += 1
            self.puntos -= 200
        else:
            print("Faltan", 200 - self.puntos, "puntos para ganar una vida extra")

    def velocidad(self):
        return 3 + self.puntos / 100