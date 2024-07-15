"""
Operadores de atribuição
= += -= *= /= //= **= %=

"""

contador_string = '-'
contador_int = 66

###

contador_string *= 10 # mutiplica a string

print(f'o valor de contador_int é: {contador_int}')
print(contador_string)
contador_int += 2 # soma o numero
print(f'soma de contador_int mais 2: {contador_int}')
contador_int = 66

contador_int *= 2 # multiplica o numero
print(f'contador_int vezes 2: {contador_int}')
contador_int = 66


contador_int -= 2 # subtrai o numero
print(f'contador_int menos 2: {contador_int}')
contador_int = 66

contador_int **= 2 # exponenciação do numero
print(f'exponenciação de contador_int por 2: {contador_int}')
contador_int = 66

contador_int //= 2 # divisao inteira do numero
print(f'contador_int divido por 2: {contador_int}')
contador_int = 66

contador_int //= 2 # divisao inteira do numero
print(f'divisao inteira de contador_int por 2: {contador_int}')
contador_int = 66

contador_int //= 2 # modulo/resto da divisao do numero
print(f'resto de divisao inteira/modulo de contador_int por 2: {contador_int}')
contador_int = 66


