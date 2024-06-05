from itertools import count
num = int(input('Digite o numero que deseja retirar a raiz quadrada: '))

cont = 1
calc = 1
while True:
    calc = cont * cont
    if calc == num:
        print(f'A raiz de {num} é {cont}')
        cont += 1

    if calc > num:
        print('Raiz não encontrada')
        break


