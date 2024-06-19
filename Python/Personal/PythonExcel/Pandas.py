import pandas as pd
#Pandas
tabela = pd.read_excel("Produtos.xlsx")

#Atualizar o multiplicador
tabela.loc[tabela["Tipo"]=="Serviço", "Multiplicador Imposto"] = 1.5

#Fazer a conta do preço Base Reais
tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]

tabela.to_excel("ProdutosPandas.xlsx", index=False)

