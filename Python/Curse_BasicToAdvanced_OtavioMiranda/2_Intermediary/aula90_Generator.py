# Generator expression, iterables e Iterators em Python
import sys
iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__() # tem __iter__ e __next
iterator = iter(iterable) # tem __iter__ e __next


# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         print('Acabou')
#         break
#     except Exception:
#         print('Erro inesperado')

lista = [n for n in range(10000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))

for n in generator:
    print(next(generator))
