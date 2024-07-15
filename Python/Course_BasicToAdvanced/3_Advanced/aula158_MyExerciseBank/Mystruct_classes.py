"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod



class Account(ABC):

    @abstractmethod
    def withdraw(self, monew: float) -> float:
        result = 0.0
        return result

    @abstractmethod
    def menu(self) -> None:
        ...


class People(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age
       
    @property
    def name(self):
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self, value):
        self.name = value
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    @abstractmethod
    def age(self, value):
        self.age = value


class Bank:
    def __init__(self):
        self.__agencies = []
        self.__customers = []
        self.__accounts = []

    @property
    def agencies(self):
        return self.__agencies
    
    @agencies.setter
    def agencies(self, value):
        self.__agencies.append(value)

    @property
    def customers(self):
        return self.__customers
    
    @customers.setter
    def customers(self, value):
        self.__customers.append(value)

    @property
    def accounts(self):
        return self.__accounts
    
    @accounts.setter
    def accounts(self, value):
       self.__accounts.append(value)


    def authentication(self, agency:str, client:str, account:str) -> str | bool:
        validation = 0
        error = ''
        if agency in self.__agencies:
            validation += 1
        
        else:
            error += 'Agencia não localizadada.\n'
        
        if client in self.__customers:
            alidation += 1
        else:
            error += 'Cliente não localizado.\n'           
              
        if account in self.__accounts:
            validation += 1
        else:
            error += 'Conta não localizada.\n'
     
        if validation == 3:
            return True
        else:
            return error          
        

class Client(People):
    def __init__(self, name, age, account):
        super().__init__(name, age)
        self.__account = account

    @People.name.setter
    def name(self, value):
        self._name = value

    @People.age.setter
    def age(self, value):
        self._age = value

    @property
    def account(self):
        return self.__account
    @account.setter
    def account(self, value):
        self.__account = value


class CurrentAccount(Account):
    def __init__(self, bank_agency, num_account):
        self._bank_agency = bank_agency
        self._num_account = num_account
        self._balance = 0.0
        self.__limit = 1000.0
        
    
    def withdraw(self, monew: float) -> float:
        calc = self._balance - monew
        if calc < 0.0:
            op = input(
                'Sem saldo em conta, quer sacar com limite especial?\n'
                f'Limite disponivel: {self.__limit}\n'
                '1 - Sim\n2 - Não'             
                )
            if op == '1':
                ...
        return
   

class SavingsAccount(Account):
    def __init__(self):
        self._bank_agency = []
        self._num_account = []
        self._balance = 0.0