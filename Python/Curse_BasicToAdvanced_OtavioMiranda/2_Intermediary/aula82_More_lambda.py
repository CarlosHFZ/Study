def executa(funcao, *args):
    return funcao(*args)

# def soma(x, y):
#     return x + y

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# duplica = cria_multiplicador(2)


multiplicador = int(input('Digite por quanto voce quer multiplicar: '))
duplica = executa(
    lambda m: lambda n: n * m,
    multiplicador
)
print(duplica(int(input('Digite aqui o valor a ser multiplicado: '))))

print(
    executa(
        lambda x, y: x + y,
        2, 10
    ),
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)