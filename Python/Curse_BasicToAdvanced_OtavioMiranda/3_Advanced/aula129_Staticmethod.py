# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Classe:
    @staticmethod
    def function_that_is_in_class(*args, **kwargs):
        print('Oi', args, kwargs)

def function(*args, **kwargs):
    print('Oi', args, kwargs)

c1 = Classe()
c1.function_that_is_in_class(1, 2, 3)
function(1, 2, 3)
Classe.function_that_is_in_class(nomeado=1)
function(nomeado=1)