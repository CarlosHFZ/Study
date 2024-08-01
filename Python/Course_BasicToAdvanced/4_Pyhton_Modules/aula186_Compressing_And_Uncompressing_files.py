# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos

PATH_ROOT = Path(__file__).parent
PATH_ZIP_DIR = PATH_ROOT / 'aula_186_diretorio_zip'
PATH_COMPRESSED = PATH_ROOT / 'aula_186_compactado.zip'
PATH_UNPACKED = PATH_ROOT / 'aula_186_descompactado'

shutil.rmtree(PATH_ZIP_DIR, ignore_errors=True)
Path.unlink(PATH_COMPRESSED, missing_ok=True)
shutil.rmtree(str(PATH_COMPRESSED).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(PATH_UNPACKED, ignore_errors=True)


# raise Exception()

# Cria o diretório para a aula]
PATH_ZIP_DIR.mkdir(exist_ok=True)


def create_files(qtd: int, zip_dir: Path):
    for i in range(qtd):
        text = 'arquivo_%s' % i
        with open(zip_dir / f'{text}.txt', 'w') as file:
            file.write(text)


create_files(10, PATH_ZIP_DIR)

# Criando um zip e adcionando arquivos
with ZipFile(PATH_COMPRESSED, 'w') as zip:
    for root, dirs, files in os.walk(PATH_ZIP_DIR):
        for file in files:
            # print(file)
            zip.write(os.path.join(root, file), file)

# Lendo arquivos de um zip
with ZipFile(PATH_COMPRESSED, 'r') as zip:
    for file in zip.namelist():
        print(file)

# Extraindo arquivos de um zip
with ZipFile(PATH_COMPRESSED, 'r') as zip:
    zip.extractall(PATH_UNPACKED)
