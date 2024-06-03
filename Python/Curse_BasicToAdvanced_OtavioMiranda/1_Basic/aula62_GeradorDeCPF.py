

def geradorCPF(num):
    for i in range(0, num):
        import random

        def verificador_final(entrada):
            return 0 if ((entrada * 10) % 11) > 9 else ((entrada * 10) % 11)

        cpf = []
        cpf_str = []
        soma_primeiro_digito = 0
        soma_segundo_digito = 0
        _ = 0
        c1 = 10
        c2 = 11
        t = 0
        for i in range(0, 10):
            if t <= 8:
                _ = random.randint(0, 9)
                cpf.append(_)
                if t == 2:
                    cpf_str.append(str(_))
                    cpf_str.append('.')
                elif t == 5:
                    cpf_str.append(str(_))
                    cpf_str.append('.')
                elif t == 8:
                    cpf_str.append(str(_))
                    cpf_str.append('-')
                else:
                    cpf_str.append(str(_))
                soma_primeiro_digito += cpf[t] * c1
                soma_segundo_digito += cpf[t] * c2
                c1 -= 1
                c2 -= 1
            if t == 9:
                t += 3
                cpf_str.append(str(verificador_final(soma_primeiro_digito)))
                soma_segundo_digito += int(cpf_str[t]) * c2
                cpf_str.append(str(verificador_final(soma_segundo_digito)))
            t += 1
        cpf_gerado = ''
        for i in cpf_str:
            cpf_gerado += i
        print(cpf_gerado)

geradorCPF(10)