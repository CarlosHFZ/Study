# Exemplo de uso dos sets
letras = set()
encerrar = True
while encerrar:
    letra = input('Digite: ')
    letras.add(letra.lower())
    print(letras)

    for i in letras:
        if 'l' == i:
            encerrar = False
            print('Parabens, descobriu a letra secreta.')