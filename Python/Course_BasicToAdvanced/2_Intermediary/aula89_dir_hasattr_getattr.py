# dir, hasattr e getattr em Python

string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo): # verifica se existe o objeto
    print('Existe upper')
    print(getattr(string, metodo)()) # pega o objeto
else:
    print('Não existe o método', metodo)

# mostra todos os objetos
print(dir(string))
