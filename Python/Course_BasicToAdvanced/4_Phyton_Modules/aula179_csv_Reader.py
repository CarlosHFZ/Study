# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

PATH_CSV = Path(__file__).parent / 'aula179.csv'
print(PATH_CSV)


with open(PATH_CSV, 'r', encoding='utf8') as file:
    # reader_ = csv.reader(file)
    reader_ = csv.DictReader(file)  # Formato em dicionario

    # next(reader_)
    # print(next(reader_))

    for row in reader_:
        # print(row[1])
        print(row['Nome'], row['Idade'])
