# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
for chave in perguntas:
    print(f'Pergunta: {chave['Pergunta']}')
    print()
    opcoes = chave['Opções']
    for i, op in enumerate(opcoes):
        print(f'{i}) {op}')
    user = input('Escolha uma opção: ')

    qtd_opcoes = len(opcoes)
    escolha_int = None
    if user.isdigit():
        escolha_int = int(user)
        

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == chave['Resposta']:
                acertos += 1
                print()
                print('Voce acertou!')
                print()
            else:
                print()
                print('Voce errou')
                print()
        else:
            print()
            print('Voce errou')
            print()
    else:
                print()
                print('Voce errou')
                print()

print(f'Voce acertou {acertos} de {len(perguntas)} perguntas')