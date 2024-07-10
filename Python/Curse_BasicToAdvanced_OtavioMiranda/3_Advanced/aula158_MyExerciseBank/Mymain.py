from Mystruct_classes import CurrentAccount, SavingsAccount, Client, Bank
import os
import random

while True:
    op = input(
        '\n1 - Cadastrar\n'
        '2 - Logar\n'
        '3 - Sair\n'
    )
    match op:
        case '1':

            user = Client(
                input('Nome: '),
                input('Idade: '),
                input('Conta: ')
            )
            print(user.name)
            print(user.account)

            bank = Bank()
            bank.agencies = input('Qual a agencia? ')
            bank.customers = user.name
            bank.accounts = user.account

            print(bank.agencies)
            print(bank.customers)
            print(bank.accounts)

        case '2':
            login = Bank()
            agency, name, conta  = input('Agencia: '), input('Name: '),input('Conta: ')
            print(agency)
            print(name, conta)
            validation = login.authentication(agency, name, conta)
            if validation is bool:
                print('Logado com sucesso')
            else:
                print(validation)
        
        case '3':
            os.system('cls')
            print('Encerrando Programa...')
            break
        case _:
            os.system('cls')
            print('Opção incorreta')