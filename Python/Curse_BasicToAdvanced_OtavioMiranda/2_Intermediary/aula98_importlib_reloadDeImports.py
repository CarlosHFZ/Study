import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    print(i)
    importlib.reload(aula98_m) 

print('Fim')