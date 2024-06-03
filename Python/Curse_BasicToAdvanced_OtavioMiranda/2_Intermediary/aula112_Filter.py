
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


# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 10
# ]


def number(num):
    return num
num = int(input('Digite: '))
num2 = int(input('Digite2: '))



def decorator(func):
    def maior_que(*args, **kwargs):
        return args['preco'] > kwargs
    return maior_que

a = decorator()

novos_produtos = filter(
    lambda p: p['preco'] > number(num),
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)