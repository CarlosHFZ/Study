# List comprehension em Python
# List comprehension é umamforma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2 
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# novos_produtos = [
#     {**produto, 'preco': produto['preco']* 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]
# print(produtos)
# print(*novos_produtos, sep='\n')

# p(novos_produtos)

# lista = [n for n in range(10) if n < 5]
# print(lista)

# antes do for é o mapeamento e depois do for e o criterio
# novos_produtos = [
#     {**produto, 'preco': produto['preco']* 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
# ]

# p(novos_produtos)

lista = []
for x in range(3):
    for y in range(3):
        for z in range(3):
            lista.append((x,y,z))

lista = [
    (x, y, z)
    for x in range(3)
    for y in range(3)
    for z in range(3)
]

lista = [
    [
        (x, letra)
        for letra in 'Luiz'
        if letra != 'L'
    ]
    for x in range(5)
]

print(lista, type(lista))