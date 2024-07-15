

# def divs(x, y):
#     return x / y
# def mult(x, y):
#     return x * y
# def quadr(x, y):
#     return x ** y

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# divisao = [divs(numero, 2) for numero in numeros]
# multiplicacao = [mult(numero, 2) for numero in numeros]
# quadrado = [quadr(numero, 2) for numero in numeros]

# novos_numeros = []
# for numero in numeros:
#     novos_numeros.append(numero)
# novos_numeros[0] = 20

# print(numeros)
# print(divisao)
# print(multiplicacao)
# print(quadrado)

# numeros_menores = [numero for numero in numeros if numero > 5]
# impares = [numero for numero in numeros if numero % 2 != 0]
# pares = [numero for numero in numeros if numero % 2 == 0]
# outro_if = [
#     numero 
#     if numero != 6 else 600
#     for numero in pares
# ]

# print(numeros)
# print(numeros_menores)
# print(impares)
# print(pares)
# print(outro_if)


# for x in range(1, 11):
#     for y in range(1, 6):
#         print(x,y)

# linhas_e_colunas = [
#     (x, y)
#     if y != 2 else (x , y * 1000)
#     for x in range(1, 11)
#     for y in range(1, 6)
#     if x != 2 
# ]

# print(linhas_e_colunas)


# string = 'Otávio Miranda'
# numero_de_letras = 3
# nova_string = '.'.join([
#     string[indice:indice + numero_de_letras]
#     for indice in range(0, len(string), numero_de_letras)
# ])

#  nova_string_2 = ''
#  for i in nova_string:
#      nova_string_2 += i
#  print(nova_string_2)

# print(nova_string)

# nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']
# novos_nomes = [
#     f'{nome[:-1].lower()}{nome[-1].upper()}'
#     for nome in nomes
# ]
# print(novos_nomes)


# numeros = [[numero, numero ** 2] for numero in range(10)]
# flat = [y for x in numeros for y in x]
# print(numeros)
# print('------------------')
# print(flat)