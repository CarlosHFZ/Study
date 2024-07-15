"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

usuario = input(
    'Que horas são agora, em inteiros por favor: '
)

try:
    hora = int(usuario)
except:
    hora = None

if hora is None:
    print('Não foi digitado a hora com numero inteiro')
elif hora > 23 or hora < 0:
    print('hora invalida')
else:
    if hora <= 11:
        print('bom dia')
    elif hora >= 12 and hora <= 17:
        print('boa tarde')
    else:
        print('Boa noite')