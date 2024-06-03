import json

caminho_arquivo = 'D:\\Carlos\\Estudos Pessoais\\python\\curso_python\\Intermediario\\'
caminho_arquivo += 'aula117.json'


pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(
        pessoa, 
        arquivo,
        ensure_ascii=False,
        indent=2,
        )

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])