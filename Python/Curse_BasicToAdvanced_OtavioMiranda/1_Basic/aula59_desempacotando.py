# Desempacotamento em chamadas
# De métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Pthon', 'é', 'Legal'

# p, b, *_, ap, u = lista
# print(p, u, ap)

# for nome in lista:
#     print(nome, end=' ')

salas = [
    # 0          1
    ['Maria', 'Helena'],  #0
    # 0
    ['Elaine', ],   # 1
    # 0
    ['Luiz', 'Joao', 'Eduarda', ], # 2
]

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

# print(salas)
print('----------------')
print(*salas, sep='\n')