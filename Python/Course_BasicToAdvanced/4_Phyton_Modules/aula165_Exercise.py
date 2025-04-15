# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta


data_formatada = '%d/%m/%Y'
data_inicio = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_inicio + delta_anos
_dif = relativedelta(data_final, data_inicio)
print(delta_anos)
print(data_final)
print(_dif.months, _dif.days)
valor = 1_000_000 / 60
c = 0
for i in range(0, 60):
    print(f'Mês: {c+1}')
    data_atual = (data_inicio + relativedelta(months=c))
    data_atual = datetime.strptime(f'{data_atual}', '%Y-%m-%d %H:%M:%S')
    print(data_atual.strftime(data_formatada))
    c += 1
    print(f'Parcela: R$ {valor:,.2f}')
    print('')


# Exercicio do professor

# valor_total = 1_000_000
# data_emprestimo = datetime(2020, 12, 20)
# delta_anos = relativedelta(years=5)
# data_final = data_emprestimo + delta_anos

# data_parcelas = []
# data_parcela = data_emprestimo
# while data_parcela < data_final:
#     data_parcelas.append(data_parcela)
#     data_parcela += relativedelta(months=+1)

# numero_parcelas = len(data_parcelas)
# valor_parcela = valor_total / numero_parcelas

# for data in data_parcelas:
#     print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

# print()
# print(
#     f'Você pegou R$ {valor_total:,.2f} para pagar '
#     f'em {delta_anos.years} anos '
#     f'({numero_parcelas} meses) em parcelas de '
#     f'R$ {valor_parcela:,.2f}.'
# )
