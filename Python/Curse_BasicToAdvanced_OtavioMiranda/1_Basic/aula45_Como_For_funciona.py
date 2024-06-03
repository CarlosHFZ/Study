"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

#texto = 'Luiz'.__iter__()
#mesma coisa
# texto = iter('Luiz') 


# print(texto.__next__()) #L
# print(texto.__next__()) #u
# print(texto.__next__()) #i
# print(texto.__next__()) #z


# Mesma coisa
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

# for letra in texto
texto = 'Luiz' # iterável
# iterador = iter(texto) # iterator

# como o for funciona por baixo dos panos
# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

# esse é o for descrito com o while acima:
for letra in texto:
    print(letra)


