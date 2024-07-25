# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

PATH_CSV = Path(__file__).parent / 'aula180.csv'

list_customers = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

# list_customers = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]

with open(PATH_CSV, 'w', encoding='utf8') as file:
    # name_colluns = list_customers[0].keys()
    name_colluns = ['Nome', 'Endereço']
    writer_ = csv.DictWriter(
        file,
        fieldnames=name_colluns
    )
    writer_.writeheader()

    for customer in list_customers:
        print(customer)
        writer_.writerow(customer)
# with open(PATH_CSV, 'w', encoding='utf8') as file:
#     # name_colluns = list_customers[0].keys()
#     name_colluns = ['Nome', 'Endereço']
#     writer_ = csv.writer(file)

#     writer_.writerow(name_colluns)

#     for customer in list_customers:
#         # print(customer.values())
#         # writer_.writerow(customer.values())
#         writer_.writerow(customer)
