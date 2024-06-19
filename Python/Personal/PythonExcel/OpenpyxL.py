from openpyxl import Workbook, load_workbook

planilha = load_workbook("Produtos.xlsx")

aba_ativa = planilha.active

for celula in aba_ativa["C"]:
    if celula.value == "Serviço":
        linha = celula.row
        aba_ativa[f"D{linha}"] = 1.5

planilha.save("ProdutosOpenPy.xlsx")



