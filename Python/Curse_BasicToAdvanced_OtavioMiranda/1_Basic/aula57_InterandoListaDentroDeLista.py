"""
lista de listas e seus indices
"""

salas = [
    # 0          1
    ['Maria', 'Helena'],  #0
    # 0
    ['Elaine', ],   # 1
    # 0
    ['Luiz', 'Joao', 'Eduarda', ], # 2
]
# print(salas[2][2]) #pinta 'Eduarda'


for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)