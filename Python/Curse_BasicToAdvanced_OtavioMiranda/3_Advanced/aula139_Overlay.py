# super() é a super classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliete)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPPOIS DO UPPER')
#         return retorno
# string = MinhaString('Luiz')


# print(string.upper())

class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('EI, burlei o sistema')
        
    def metodo(self):
        # super(C, self).metodo() # B
        # e o mesmo que:
        # super().metodo() -> não precisa colocar parametro, se vc buscar o super dessa classe que estamos
        # super(B, self).metodo() # A
        # super(A, self).metodo()

        #Pode fazer dessa maneira mas o recomendado e utilizar a nomenclatura super
        B.metodo(self)
        A.metodo(self)
        print('C')


c = C('Atributo', 'Oualquer')
# print(c.atributo)
# print(c.outra_coisa)

c.metodo()

# print(C.mro())
# print(B.mro())
# print(A.mro())
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()