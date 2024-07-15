# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# people = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 900
# }

# setdefault - adiciona valor se a chave não existe
# people.setdefault('idade', 0)
# print(people['idade'])

# len - quantas chaves
# print(len(people))

# keys - iterável com as chaves
# print(list(people.keys()))

# values - iterável com os valores
# print(list(people.values()))

# items - iterável com chaves e valores
# print(list(people.items()))

# for chave in people.keys():
#     print(chave)

# for valor in people.values():
#     print(valor)

# for chave, valor in people.items():
#     print(chave, valor)
