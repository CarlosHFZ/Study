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
from pypdf import PdfReader, PdfWriter

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


# page0 = reader.pages[0]

page0 = reader.pages[0]
image0 = page0.images[0]


# print(page0.images)
# print(page0.images[0])
# print(len(page0.images))

# with open(NEW_FOLDER / image0.name, 'wb') as fp:
#     fp.write(image0.data)


# writer = PdfWriter()

# with open(NEW_FOLDER / 'page0.pdf', 'wb') as archive:

#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(archive)

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NEW_FOLDER / f'page{i}.pdf', 'wb') as archive:
        writer.add_page(page)
        writer.write(archive)


files = [
    NEW_FOLDER / 'page0.pdf',
    NEW_FOLDER / 'page1.pdf',
]
merger = PdfWriter()
for file in files:
    merger.append(file)  # type: ignore

merger.write(NEW_FOLDER / 'merged0.pdf')  # type: ignore
merger.close()   # type: ignore
