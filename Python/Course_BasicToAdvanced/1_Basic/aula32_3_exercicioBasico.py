
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

usuario = input(
    'Digite seu primeiro nome: '
)
letras = len(usuario)

if letras <= 4:
    print('Seu nome é curto')
if letras >= 5 and letras <= 6:
    print('Seu nome é normal')
if letras > 6:
    print('Seu nome é muito grande')