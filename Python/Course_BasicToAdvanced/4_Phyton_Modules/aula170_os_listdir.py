# os.listdir para navegar em caminhos
# /Carlos/Deposito/Fotos
# D:\Carlos\Deposito\Fotos
# caminho = r'D:\\Carlos\\Deposito\\Fotos'
import os
caminho = os.path.join('\\Carlos', 'Deposito')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue

    for item in os.listdir(caminho_completo_pasta):
        print('  ', item)
