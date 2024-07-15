# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

# import sys

# sys.setrecursionlimit(1002)
# def recursiva(inicio=0, fim=4):

#     print(inicio, fim)

#     # Caso base
#     if inicio >= fim:
#         return fim
    
#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva(0, 1000))


def factorial(n):
    if n <= 1:
        print(f'NF:{n}')
        return 1
    print(f'N:{n}')
    return n * factorial(n - 1)

print(factorial(5))

print()
def fun(inicio = 0, fim = 4):
    print(inicio)
    if inicio >= fim:
        return 'acabou'
    inicio += 1
    return "x" + fun(inicio)
 
print(fun()) # por incrivel que pareca o retorno não sera "acabou"
             # e sim "xxxxacabou" por caulca da mesma logica do fatoria!
             # "acabou" é o retorno da ultima execulção de acabou e no
             # print nos temos a primeira execulção.