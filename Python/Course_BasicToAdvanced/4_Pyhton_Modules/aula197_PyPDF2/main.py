# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader

ROOT_FOLDER = Path(__file__).parent
ORIGINALS_FOLDER = ROOT_FOLDER / 'pdf_originals'
NEW_FOLDER = ROOT_FOLDER / 'new_archives'

BACEN_RELATORY = ORIGINALS_FOLDER / 'R20250221.pdf'

NEW_FOLDER.mkdir(exist_ok=True)

reader = PdfReader(BACEN_RELATORY)

# print(len(reader.pages))

# for page in reader.pages:
#     print(page)
#     print()


page0 = reader.pages[0]

# print(page0.extract_text())
print(page0.images)
