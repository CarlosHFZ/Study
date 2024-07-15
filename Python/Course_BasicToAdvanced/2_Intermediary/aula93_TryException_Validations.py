# Try, except, else e finally

try:

    print('Linha 1')
    a = 18
    b = 0
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Variavel não está definida')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)
except Exception:
    print('ERROR DESCONHECIDO.')

print('CONTINUAR')