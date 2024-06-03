"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'carro'
deposito_letras = ''
tentativas = 0


while True:
    
    chute = input('Digite seu chute:  ')

    if len(chute) > 1:
        print('\nVocê digitou mais de uma letra, falor digitar somente uma!\n')
        continue
    if not chute.isalpha():
        print('\nDigite apenas letras!\n')
        continue
    
    tentativas += 1

    if chute in palavra_secreta:
        deposito_letras += chute

    palavra = ''
    for i in palavra_secreta:
        if i in deposito_letras:
            palavra += i
        else:
            palavra += '*'

    if '*' in palavra:
        print(palavra)
    else:
        os.system('cls')
        print(f'PARABENS!\nVOCÊ ACERTOU A PALAVRA\nCOM {tentativas} CHUTES\nA PALAVRA ERA ({palavra_secreta}) ')        
        break
         





