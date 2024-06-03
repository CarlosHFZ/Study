# map, partial, GeneratorType e esgotamento de Iterators
from functools import partial

# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumantar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumantar_dez_porcento = partial(
    aumantar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     {**p,
#         'preco': aumantar_dez_porcento(p['preco'])} 
#     for p in produtos
# ]

def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumantar_dez_porcento(
            produto['preco']
            )
        } 
# faz a mesma coisa que uma list comprehension faz
novos_produtos = map(
    muda_preco_de_produtos,
    produtos
)

# print_iter(produtos)
# print_iter(novos_produtos)

# map pode ser utilizado com funçôes lamda
# print(
#     list(map(
#         lambda x: x* 3,
#         [1, 2, 3, 4]
#     ))
# )