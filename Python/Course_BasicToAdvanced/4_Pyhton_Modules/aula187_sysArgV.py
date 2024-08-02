# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

arguments = sys.argv
qtd_arguments = len(arguments)

if qtd_arguments <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos {arguments[1:]}')
        print(f'Faça alguma coisa com {arguments[1]}')
        print(f'Faça outra coisa com {arguments[2]}')
    except IndexError:
        print('Faltam argumentos')
