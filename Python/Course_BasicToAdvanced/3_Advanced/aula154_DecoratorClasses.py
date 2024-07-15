# Classes decoradoras (Decorator classes)
from typing import Any


class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador
    
    def __call__(self, func):
        def interna(*args, **kwargs):   
            resultado = func(*args, **kwargs)  
            return self._multiplicador * resultado
        return interna


@Multiplicar(5)
def soma(x, y):
    return x + y

dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)