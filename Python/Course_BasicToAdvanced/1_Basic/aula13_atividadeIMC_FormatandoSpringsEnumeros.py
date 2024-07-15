'''
    Calculo do IMC
    IMC = peso / (altura x altura)

'''


nome = 'Carlos Henrique'
altura = 1.72
peso = 62
imc = peso / altura**2

#f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc è'
linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)

#print(nome,'tem',altura,'\n','pesa ',peso,' quilos e seu IMC é','\n',imc)