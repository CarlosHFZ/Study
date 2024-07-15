# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradoras são "Syntax Sugar" (Açucar sintático)

def create_function(function):
    def intern(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = function(*args, **kwargs)
        print(f'Seu resultado foi {resultado}')
        print('Ok, agora você foi decorada')
        return resultado
    return intern

@create_function # Automatizar
def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')


# check_param = create_function(inverte_string) # Sem @create_function
invertida = inverte_string('Carlos') # Com @create_function
print(invertida)