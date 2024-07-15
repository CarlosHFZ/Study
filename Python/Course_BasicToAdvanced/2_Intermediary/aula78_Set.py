# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set() # vazio
# s1 = {'Luiz', 1, 2, 3} # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1 ,2 , 3, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = s1 = {1, 2, 3, (123, )} # set so aceita valores imutaveis, nesse caso tupla é imutavel
# print(s1)
# print(3 not in s1)
# for numero in s1:
#     print(numero)


# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
# print(s1)

# Operadores úteis:


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # união | união (union) - Une
s3 = s1 & s2 # intersecção & (intersection) - Itens presentes em ambos
s3 = s2 - s1 # diferença - Itens presentes apenas no set da esquerda
s3 = s2 ^ s1 # diferença simétrica ^ - Itens que não estão em ambos

print(s3)