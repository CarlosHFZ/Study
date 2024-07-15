"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R%.2f' % (nome, preco) # % insere algo de acordo com o especificado, obs: $ '.2' f entre parenteses (.2) é o numeor de casas decimais
print(variavel)
print('O hexadecimal de %d é %08x' % (10004, 10004)) #mostra um numero int e ele em hexadecimal, obs: %08x o 08 e o tamanho das casas do hexadecimal