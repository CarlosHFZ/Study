
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

usuario = input(
    'Me informe um numero inteiro, estão irei dizer se ele é par ou impar.'
    '\nDigite: '
)
# validando se oque foi digitado foi um numero
try:
    numero = int(usuario) # conversao do que foi digitado para int
except:
    try: # caso o usuario tenha digitado numeros com ponto essa e outra verificação para tratar
        numero = float(usuario) # conversao do que foi digita para float
        numero = False
    except:
        numero = None

if numero is None: # caso o que foi digitado não foi numero inteiro e nem numero com pontos, cai aqui.
    print('Isso não é um numero')
elif numero is False: # caso oque o usuario digitou for numero com ponto cai aqui
    print('Isso é um numero com ponto flutuante, favor me informar um numero inteiro.')
else:
    calculo = (numero % 2) # criei a variavel calculo para pegar o resto da divisao  
    if calculo == 0: # se o resto da divisao for igual a zero o numero é par
        print(
            f'O numero: {numero} é par.'
        )
    else: # se o resto da divisao for maior que 0 o numero é impar
        print(
            f'O numero: {numero} é impar.'
        )

