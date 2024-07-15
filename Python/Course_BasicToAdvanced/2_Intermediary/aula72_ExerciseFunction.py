# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

entrada = 1,2,3,4,5,6,7,8,9
resultado = 0
def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
resultado = multiplicacao(*entrada)
print(resultado)


def par_impar(num):
    if (num % 2) == 0:
        return f'{num=} é par'
    return f'O numero {num} é impar'

print(par_impar(17))