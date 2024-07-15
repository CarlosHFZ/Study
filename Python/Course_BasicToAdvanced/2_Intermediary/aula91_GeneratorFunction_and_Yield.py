# Introdução ás Generator functions em Python
# generator = (n for n in range(100000))

def generator(n=0, maximum=10):

    # yield 1 # Pausar | Generation Function
    # print('Continuando...')
    # yield 2 # Pausa novamente
    # print('Mais uma...')
    # yield 3
    # print('Vou terminar')
    # return 'ACABOU'
    while True:
        yield n
        n += 1
        if n >= maximum:
            return

        

gen = generator(maximum=10000)
for n in gen:
    print(n)