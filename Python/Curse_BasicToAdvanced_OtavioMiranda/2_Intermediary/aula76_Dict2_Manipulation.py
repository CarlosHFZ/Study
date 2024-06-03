#  Manipulando chaves e valores em dicionários

# people = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua':'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ],
# }

people = {}

key = 'nome'
people[key] = 'Luiz Otávio'
people['sobrenome'] = 'Luiz Otávio'
liste = []

print(people[key])

people[key] = 'Maria'
del people['sobrenome']
print(people)
print(people['nome'])

if people.get('sobrenome') is None:
    print('Não existe')
else:
    print(people['sobrenome'])