"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
# print(len(variavel))

print(variavel[0:len(variavel):2])
print(variavel[::-1]) #inverte a variavel

# print(variavel[4:])
# print(variavel[:5])
# print(variavel[-8:-2])