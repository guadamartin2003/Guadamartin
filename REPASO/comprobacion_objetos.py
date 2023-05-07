class Caballo:
  def __init__(self, una_energia, una_raza, kms):
    self.energia = una_energia
    self.raza = una_raza
    self.kms = kms

  def comer(self, gramos):
    self.energia += gramos * 2

  def esta_feliz(self):
    return True

  def galopar(self, kms):
    self.energia -= kms

  def kilometros_recorridos(self, kms):
     self.kms += kms

caballo = Caballo(50, "Pura Sangre", 0)

# Imprimir la energía del caballo
print("Energía del caballo:", caballo.energia)

# Imprimir la raza del caballo
print("Raza del caballo:", caballo.raza)

# Imprimir si el caballo está feliz
print("¿El caballo está feliz?", caballo.esta_feliz())

# Comer 5 kilogramos de alimento
caballo.comer(5)

# Imprimir la nueva energía del caballo después de comer
print("Nueva energía del caballo después de comer:", caballo.energia)

# Galopar 10 kilómetros
caballo.galopar(10)

# Imprimir la energía del caballo después de galopar
print("Energía del caballo después de galopar:", caballo.energia)

# Registrar 15 kilómetros recorridos
caballo.kilometros_recorridos(15)

# Imprimir los kilómetros totales recorridos por el caballo
print("Kilómetros totales recorridos por el caballo:", caballo.kms)
