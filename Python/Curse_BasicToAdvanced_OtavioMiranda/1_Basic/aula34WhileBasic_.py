"""
Repetições
while (enquanto)
Execute uma ação equanto uma condição for verdadeira
"""
condicao = True
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu no nome é {nome}')
    
    if nome == 'sair':
        break

print('acabou')