# Ordem dos decoradores

def parametros_decorador(nome=None):
    def decorador(func):
        print('Decorador:', nome)
        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
def mult(x, y):
    return x * y
@parametros_decorador(nome='1')
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10,5)
multiplica = mult(20,20)
print(multiplica)
print(dez_mais_cinco)
