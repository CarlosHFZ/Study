# Escopo da classe e de métodos da classe

class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome
    
    def comendo(self, *args):
        return f'{self.nome} está comendo {args}'
    
    def executar(self, *args):
        return self.comendo(*args)


# print(Animal.nome)

leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('Maça','Ostra','Mamute'))