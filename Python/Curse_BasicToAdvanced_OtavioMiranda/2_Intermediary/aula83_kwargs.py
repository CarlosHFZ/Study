# Eempacotamento e dsempacotamento de dicionarios

# a, b = 1, 2
# a, b = b, a

# print(a, b)


# (a1, a2), b = pessoa.items()

# print(a1, a2)
# print(b)


# for chave, valor in pessoa.items():
#     print(chave, valor)



pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)   
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1,2,nome='Joana', qlq=123, tu=78)
mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

# mostro_argumentos_nomeados(**configuracoes)