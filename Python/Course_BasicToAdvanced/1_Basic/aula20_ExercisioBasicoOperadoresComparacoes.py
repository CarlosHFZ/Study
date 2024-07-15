primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(
        f'O primeiro valor={primeiro_valor} é maior ' 
        f'que o segundo valor={segundo_valor}'
    )
elif primeiro_valor == segundo_valor:
    print(
        f'O primeiro valor={primeiro_valor} é igual ao ' 
        f'segundo valor={segundo_valor}'
    )
else:
    print(
        f'O segundo valor={segundo_valor} é maior que o ' 
        f'primeiro valor={primeiro_valor}'
    )

