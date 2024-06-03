'''
split e join com list e str
split - divide uma string
join = une uma string
'''

frase =    'Olha só que   , coisa interessante        '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) #lstrip e rstrip

# print(lista_frases_cruas)
# print(lista_frases)

freases_unidas = '-------'.join(lista_frases)
print(freases_unidas)