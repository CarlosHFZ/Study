# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

# def create_function(function):
#     def intern(*args, **kwargs):
#         print(args, kwargs)
#         for arg in args:
#             is_string(arg)
#         resultado = function(*args, **kwargs)
#         print(f'Seu resultado foi {resultado}')
#         return resultado
#     return intern


# def inverte_string(string):
#     return string[::-1]

# def is_string(param):
#     if not isinstance(param, str):
#         raise TypeError('Param deve ser uma string')


# check_param = create_function(inverte_string)
# invertida = check_param('Carlos')
# print(invertida)



def creat_function(func):
    def intern(*args, **kwargs):
        resultado = f'{func(*args, **kwargs)} {modelo()}'

        return f'Conseguimos localizar o veiculo {resultado}'

    return intern    


@creat_function
def carro(carro):
    return f'{carro} Seminovo'

def modelo():
    return f'Do modelo: 2001'


a = carro('Monza')

print(a)
