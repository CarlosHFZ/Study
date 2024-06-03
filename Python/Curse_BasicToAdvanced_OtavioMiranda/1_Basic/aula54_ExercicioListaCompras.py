"""
Faça uma lista de compras com listas
o usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de
indices inexistentes na lista.

"""
import os
lista = []


while True:
    print('Selecione uma opção')
    usuario = input('[i]-Inserir [a]-Apagar [l]-Listar [e]-Encerrar: ').lower()
    if usuario == 'i':
        os.system('cls')
        lista.append(input('Digite oque deseja adicionar a lista: '))
    elif usuario == 'a':
        if len(lista) == 0:
            os.system('cls')
            print('Voce não tem nada para apagar da lista')
        else:
            while usuario:
                try:
                    usuario = int(input('Digite o indice a ser apagado: '))
                    lista.pop(usuario)
                    usuario = False
                except ValueError:
                    os.system('cls')
                    print('Por favor digite um numero inteiro')
                    usuario = True                           
                except IndexError:
                    os.system('cls')
                    print('Valor de indice não existe na lista')
                    usuario = True                           
    elif usuario == 'l':
        if len(lista) == 0:
            os.system('cls')
            print('Lista está vazia')    
        for indice, name in enumerate(lista):
            print(indice, name)
    elif usuario == 'e':
        os.system('cls')
        print('Programa encerrado')
        break
    else:
        os.system('cls')
        print('Opção incorreta')
        
    