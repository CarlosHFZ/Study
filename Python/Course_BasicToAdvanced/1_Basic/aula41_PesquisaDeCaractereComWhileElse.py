""" while/else """

string = input('Escreva alguma coisa: ')

i = 0
c = 0
while i < len(string):
    letra = string[i]
    if (i + 1) == len(string):
        if letra == ' ':
            c +=1
            break
        else:
            break
    if letra == ' ':
        c += 1

    i += 1

else:
    print('Não encontrei espaços no que foi digitado')
print(f'Foi encotrado {c} espaços em {string}')