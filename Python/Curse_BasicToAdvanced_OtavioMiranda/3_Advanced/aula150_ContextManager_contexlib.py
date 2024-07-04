# Context Manager com função - Criando e Usando gerenciadores de context
from contextlib import contextmanager


@contextmanager
def my_open(cominho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(cominho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro', e)
    finally:    
        print('Fechando arquivo')
        arquivo.close()


with my_open('aula150.txt', 'w')  as arquivo:
    arquivo.write('Linha 1\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)