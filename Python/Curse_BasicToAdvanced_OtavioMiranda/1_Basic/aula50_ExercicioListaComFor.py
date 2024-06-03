'''
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz

'''

# minha resolução
# lista = ['Maria', 'Helena', 'Luiz']
# c = 0
# for nome in lista:
#     lista[c] = f'{c} {nome}'
#     print(lista[c])
#     c += 1

# resolução do professor
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))