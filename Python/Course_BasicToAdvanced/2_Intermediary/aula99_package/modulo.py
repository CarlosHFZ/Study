__all__ = [
    'variavel', # __all__ diz ao python quando alguem importar tudo "*" vai
    'soma_do_modulo'            # estar disponival so oque estiver disponivel no __all__
]
from aula99_package.modulo_b import fala_oi
variavel = 'Algumas Coisa'
outra_variavel = 'Nada'

def soma_do_modulo(x, y):
    return x + y

fala_oi()