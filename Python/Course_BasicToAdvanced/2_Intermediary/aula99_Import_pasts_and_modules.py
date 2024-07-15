# from sys import path
# # print(*path, sep='\n')


# # Diferenter maneiras de importar modulos

# import aula99_package.modulo
# print(aula99_package.modulo.soma_do_modulo(1,2))


# from aula99_package.modulo import * # Má pratica # importa tudo do modulo indicado
# # print(soma_do_modulo(1, 2)) # o __all__ restringiu essa função
# print(variavel) # variavel é possivel pois foi indicada dentro do __all__


# from aula99_package import modulo
# print(modulo.soma_do_modulo(1, 2))


# from aula99_package.modulo import soma_do_modulo, outra_variavel # Método mais indicado
# print(soma_do_modulo(1,2))
# print(outra_variavel)


# from aula99_package.modulo import soma_do_modulo, fala_oi
# print(__name__)
# fala_oi()

from aula99_package import fala_oi, soma_do_modulo

fala_oi()
print(soma_do_modulo(3,5))

