# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_exterto(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    
    def __del__(self):
        print('APAGANDO, ', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print('APAGANDO, ', self.rua, self.numero)


cliente = Cliente('Maria')
cliente.inserir_endereco('Av Brasil', 54)
cliente.inserir_endereco('Rua b', 6458)
endereco_externo = Endereco('Av Saudade', 1215478)
cliente.inserir_endereco_exterto(endereco_externo)
print("-----------")
cliente.listar_enderecos()
# print(cliente.enderecos[0].rua, cliente.enderecos[0].numero)
# print(cliente.enderecos[1].rua, cliente.enderecos[1].numero)

print("-----------")

del cliente


print(endereco_externo.rua, endereco_externo.numero)
print('AQUI TERMINA MEU CÓDIGO')
print("-----------")