"""
Introdução ao desempacotamento + tuples (tuplas)
"""


# _, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
# print(nome)

nomes = ['Maria', 'Helena', 'Luiz']
nomes[1] = 'outro'
_, _, nome, *resto = nomes
print(nomes)
print(nome)