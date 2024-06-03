# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(lista1, lista2):
#     limite = min(len(lista1), len(lista2))
#     return [
#         (lista1[i],lista2[i]) for i in range(limite)
#     ]

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']


# print(zipper(lista1,lista2))


print(list(zip(lista1,lista2))) # funcao que junta a maior lista na menor

from itertools import zip_longest

print(list(zip_longest(lista1,lista2, fillvalue='SEM CIDADE')))  # funcao que junta a menor lista na maior, 
                                                                 # incluindo o valor None(ou indicar um valor com fillvalue) nos que não completar
