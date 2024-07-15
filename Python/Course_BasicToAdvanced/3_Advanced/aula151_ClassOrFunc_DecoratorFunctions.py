# Funções decoradoras e decoradores com classes

# A função repr pode ser feita dessa maneira
# def adciona_repr(cls):
#     def meu_repr(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr  
#     cls.__repr__ = meu_repr
#     return cls     

# Ou dessa maneira
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr  

def adciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls     




# class MyReprMixin:   
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr   


@adciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adciona_repr  
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    
# Time = adciona_repr(Time)
brasil = Time('Brasil')
portugal = Time('Portugal')

# Planeta = adciona_repr(Planeta)
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)