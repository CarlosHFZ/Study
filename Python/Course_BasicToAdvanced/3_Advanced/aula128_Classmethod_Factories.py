# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("Hey")

    @classmethod
    def create_with_50_age(cls, nome):
        return cls(nome, 50)

    @classmethod
    def create_without_name(cls, nome):
        return cls("Anônima", 50)



p1 = Pessoa("João", 34)
p2 = Pessoa.create_with_50_age("Helena")
p3 = Pessoa("Anônima", 23)
p4 = Pessoa.create_without_name(25)

print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()