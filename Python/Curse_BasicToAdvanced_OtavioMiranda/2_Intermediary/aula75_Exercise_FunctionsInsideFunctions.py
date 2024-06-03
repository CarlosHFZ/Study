# Exercícios
# Crie funções que duplicam, tripplicam e quadruplicam
# o número recebido como parâmetro.

def create_multipliers(multiplier):
    def multiply(number):
        return (number * multiplier)     
    return multiply


number = int(input('Você deseja multiplicar qual numero? '))
multiplier = int(input('Multiplicar quantas vezes? '))
calculator = create_multipliers(multiplier)

print(f'{multiplier} x {number} = {calculator(number)}')




