# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois cire novamente as instância
# da classe com dados salves
# Faça em arquivos separadas
import json
import os


diretorio_atual = os.path.dirname(os.path.abspath(__file__))
CAMINHO_ARQUIVO = os.path.join(diretorio_atual, './aula127_ExerciseSAVEJSON.json')

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Carlos', 11)

bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding="utf-8") as arquivo:
        print('Fazer DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('ELE È O __main__')
    fazer_dump()