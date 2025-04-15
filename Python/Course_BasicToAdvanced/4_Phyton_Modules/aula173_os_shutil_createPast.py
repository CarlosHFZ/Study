# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')

DESKTOP = os.path.join(HOME, 'OneDrive')
DESKTOP = os.path.join(DESKTOP, 'Área de Trabalho')

PASTA_ORIGINAL = os.path.join(DESKTOP, 'Saves Minecraft 1.20.4')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminho_novo_arquivo, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        print(caminho_novo_arquivo)
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
