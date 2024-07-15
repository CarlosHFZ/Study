# Decoradores com parâmetros

def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')
        def aninhada(*args, **kwargs):
            print('Aninhada')
            res = func(*args, **kwargs)            
            return res
        return aninhada
    
    return fabrica_de_funcoes

@fabrica_de_decoradores(a=1, b=2, c=10)
def soma(x, y=None):
    return x + y

# decoradora = fabrica_de_decoradores()
# multiplica = decoradora(lambda x,y: x * y )
multiplica = fabrica_de_decoradores()(lambda x, y:  x * y) # da pra fazer em uma linha só dessa forma
somar_todos_os_numeros = fabrica_de_decoradores(a=1)(lambda *args: sum(args) )

# print(somar_todos_os_numeros(2,2,2))

# dez_mais_cinco = soma(10, y=5)
# dez_vezes_cinco = multiplica(10, 5)
# print(dez_mais_cinco)
# print(dez_vezes_cinco)