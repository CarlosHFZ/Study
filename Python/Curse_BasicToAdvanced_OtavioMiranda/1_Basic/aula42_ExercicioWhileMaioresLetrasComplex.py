
"""
'2O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guida van Rossum'

"""
frase = input('Digite: ')
i = 0
maior_qtd_letra = 0
letra_mais = ""

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_atual = frase.count(letra_atual)

    if maior_qtd_letra <= qtd_letra_atual :
            if qtd_letra_atual == maior_qtd_letra :
                if letra_atual in letra_mais:
                    i += 1
                    continue
                else:
                    letra_mais += letra_atual 
            else:            
                maior_qtd_letra  = qtd_letra_atual
                letra_mais = letra_atual
    i += 1


c = 0    
if len(letra_mais) > 1:
    print('Essas foram as letras que mais apareceram: \n')
    while c < len(letra_mais):
        print(
            f'Letra: {letra_mais[c]} '\
            f'Apareceu: {maior_qtd_letra} vezes'
        )
        c += 1
else:
    print(f'A letra que apareceu mais vezes foi: {letra_mais}, apareceu {maior_qtd_letra} vezes')

