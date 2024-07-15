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

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# Remove uma chave a sua escolha no dicionario
# nome = p1.pop('nome')
# print(nome)
# print(p1)

# Remove a ultima chave do dicionario
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)


# atualiza e adiciona as informações do dicionario
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })

# outra forma de escrever
# p1.update(nome='novo valor', idade=31)

# Mais uma forma de escrever, tanto como tupla ou como lista
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)