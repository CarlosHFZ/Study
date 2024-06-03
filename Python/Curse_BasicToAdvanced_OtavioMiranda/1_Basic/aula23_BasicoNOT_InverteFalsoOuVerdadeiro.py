# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print(f'{bool(senha)} Você não digitou nada')
else:
    print(bool(senha))
