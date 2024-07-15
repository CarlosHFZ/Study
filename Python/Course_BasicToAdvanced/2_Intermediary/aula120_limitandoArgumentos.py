# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# # oque tiver depois da / pode ser argumento nomeado, 
# atras da / é obrigado a ser argumentos posisionais
# def soma(a, b, /, x, y):
#     print(a + b + x + y)

# soma(1, 2, 3, y=3)


# antes da / deve ser posisinal, depois do * deve ser nomeado!
def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b * c)

soma(1, 2, c=3, nome='Joao', sobrenome='Santos' )
