"""
enumerate - enumera iteráveis (indices)

"""
# [(0,'Maria'),(1, 'Helena'),(2, 'Luiz')]
nomes = ['Maria', 'Helena', 'Luiz']
nomes.append('João')

# lista_enumerada = enumerate(nomes)
# print(next(lista_enumerada))

# lista_enumerada = list(enumerate(nomes, start=19))
# print(lista_enumerada)

for indice, nome in enumerate(nomes):
    print(indice, nome, nomes[indice])

# for indice, nome in enumerate(nomes):
#     print(indice, nome)

# for item in enumerate(nomes):
#     indice, nome = item
#     print(indice, nome)

# for item in enumerate(nomes):
#     print('FOR da tupla')
#     for valor in item:
#         print(f'\t{valor}')


