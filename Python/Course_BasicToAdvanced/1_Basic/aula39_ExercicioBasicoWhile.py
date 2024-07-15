"""
Iterando strings com while
"""


#.......02345678910
nome = 'Luiz Otávio' # Iteráveis
tamanho_nome = len(nome)
nova_string = ""

contador = 0

while contador < (len(nome)):
    nova_string += '*' + nome[contador]
    contador += 1
    
print(nova_string)
    






