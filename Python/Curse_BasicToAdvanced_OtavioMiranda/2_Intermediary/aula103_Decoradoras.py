# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def create_function(function):
    print('create_function')
    def intern(*args, **kwargs):
        print('intern antes de executar isString')
        for arg in args:
            is_string(arg)
        print('intern depois de executar isString')
        resultado = function(*args, **kwargs)
        print(f'Seu resultado foi {resultado}')
        print('Ok, agora você foi decorada')
        return resultado
    print('create function logo antes do retorno')
    return intern


def inverte_string(string):
    print('InvertString')
    return string[::-1]

def is_string(param):
    print('IsString')
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')


check_param = create_function(inverte_string)
invertida = check_param('Carlos')
print(invertida)