"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import re
import os
cpf_digitado = ''
deposito_numeros = ''
total_pri_digito = 0
verificador_sinais = ''
def verificador_final(entrada):
    return 0 if ((entrada * 10) % 11) > 9 else ((entrada * 10) % 11)
    

# Poderia ter usado esse método para converter o CPF com pontos e traço para so numeros:
# ajustar = re.sub(r'[^0-9]','',cpf_digitado)
while True:
    cpf_digitado = input('Digite o CPF com pontos e traço: ')
    contador_regressivo_1 = 10
    for i in cpf_digitado:
        try:
            if verificador_sinais == '..-':
                break
            else:
                total_pri_digito += (int(i) * contador_regressivo_1)
                deposito_numeros += i
                
                contador_regressivo_1 -= 1           
        except TypeError:
            verificador_sinais += i
        except ValueError:
            verificador_sinais += i
    if verificador_sinais != '..-' or len(cpf_digitado) != 14:
        os.system('cls')
        print('CPF digitado incorretamente: ', cpf_digitado)
        verificador_sinais = ''
        total_pri_digito = 0
        contador_regressivo_1 = 10
        deposito_numeros = ''
    else:
        break

deposito_numeros += str(verificador_final(total_pri_digito))
total_seg_digito = 0

contador_regressivo_2 = 11
for i in deposito_numeros:
    total_seg_digito += (int(i) * contador_regressivo_2)
    contador_regressivo_2 -= 1

deposito_numeros += str(verificador_final(total_seg_digito))

cpf_calculado = ''
c = 0


for i in range(0,11):
    if c == 3 or c == 6:
        cpf_calculado += '.'
    if c == 9:
        cpf_calculado += '-'
    cpf_calculado += str(deposito_numeros[i])
    c += 1

if cpf_digitado == cpf_calculado:
    primeiro_digito = deposito_numeros[0]
    repeticao = primeiro_digito * len(deposito_numeros)
    if deposito_numeros == repeticao:
        os.system('cls')
        print('CPF inválido')
    else:
        os.system('cls')
        print(f'O CPF "{cpf_digitado}" é válido')
else:
    os.system('cls')
    print(f'O CPF "{cpf_digitado}" é invalido')








    



                
        


