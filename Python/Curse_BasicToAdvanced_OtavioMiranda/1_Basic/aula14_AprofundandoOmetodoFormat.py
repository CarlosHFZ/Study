a = 'AAAA'
b = 'BBBB'
c = 1.1
string = 'a={0} a={0} b={nome2}  b={nome2} c={nome3:.2f}'
formato = string.format(
    a, nome2=b, nome3=c
    
    )

print(formato)