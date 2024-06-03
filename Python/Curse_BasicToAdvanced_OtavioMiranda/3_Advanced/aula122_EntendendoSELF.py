# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a prórpia instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

# string = 'Carlos'
# print(string.upper())

fusca = Carro('Fusca')
# print(fusca.nome)
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro(nome='Celta')
# print(celta.nome)
celta.acelerar()
Carro.acelerar(celta)