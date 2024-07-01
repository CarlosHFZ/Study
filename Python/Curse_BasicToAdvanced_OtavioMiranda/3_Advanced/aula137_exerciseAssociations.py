# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela



class Carro():
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor


    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    def mostrar(self):
        print(
                f'Carro: {self.nome}\n'
                f'Motor: {self._motor.nome if self._motor else "Nenhum motor definido"}\n'
                f'Fabricante: {self._fabricante.nome if self._fabricante else "Nenhum fabricante definido"}\n'
            )


class Motor():
    def __init__(self, nome):
        self.nome = nome


class Fabricante():
    def __init__(self, nome):
        self.nome = nome


gol = Carro('Gol')   
volkswagen = Fabricante('Volkswagen')
gol.fabricante = volkswagen

gol_motor = Motor('1.0')
gol.motor = gol_motor

gol.mostrar()


gol_turbo = Carro('Gol Turbo')   
volkswagen = Fabricante('Volkswagen')
gol_turbo.fabricante = volkswagen

gol_turbo_motor = Motor('2.0')
gol_turbo.motor = gol_turbo_motor

gol_turbo.mostrar()


fiat_uno = Carro('Fiat Uno')   
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat

fiat_uno_motor = Motor('1.0')
fiat_uno.motor = fiat_uno_motor

fiat_uno.mostrar()

civic = Carro('Civic')   
fiat = Fabricante('Fiat')
civic.fabricante = fiat

civic_motor = Motor('1.0')
civic.motor = civic_motor

civic.mostrar()
