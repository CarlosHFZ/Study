# Problema dos parâmetros mutáveis em funções Python

def adciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adciona_cliente('luiz')
adciona_cliente('Joana', cliente1)
adciona_cliente('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adciona_cliente('Carlos')
adciona_cliente('Henrique', cliente2)


cliente3 = adciona_cliente('Moreira')
adciona_cliente('Vivi', cliente3)




print(cliente1)
print(cliente2)
print(cliente3)