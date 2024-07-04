# Funções decoradoras e decoradores com classes

def adciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr  
    cls.__repr__ = meu_repr
    return cls   

def meu_planeta(metodeo):
    def interno(self, *args, **kwargs):
        resultado = self.falar_nome()
        return resultado
    return interno  

@adciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adciona_repr  
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())