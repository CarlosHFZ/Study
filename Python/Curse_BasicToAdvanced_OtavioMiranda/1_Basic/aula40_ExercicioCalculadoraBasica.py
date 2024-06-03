""" Calculadora com while"""


while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador: ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None



    if numeros_validos is None:
        print('Um ou ambos os númenos são invalidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

     ###
    soma = (num_1_float + num_2_float)
    subtração = (num_1_float - num_2_float)
    divisao = (num_1_float / num_2_float)
    multiplicação = (num_1_float * num_2_float)
    resposta = f'{num_1_float} {operador} {num_2_float}'

    if operador == '+':
        print(f'{resposta} = {soma}')

    elif operador == '-':
        print(f'{resposta} = {subtração}') 

    elif operador == '/':
        print(f'{resposta} = {divisao}')   

    elif operador == '*':
        print(f'{resposta} = {multiplicação}') 
    else:
        print('Nunca deveria chegar aqui')  

    sair = input('Quer sair? [s] para sim: ').lower().startswith('s')
    if sair is True:
        break