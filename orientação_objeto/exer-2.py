#exercicío 1-Na classe, ContaBancaria, converta saldo para uma atributo privado. Crie um método setter e um getter para acessar 
#e modificar essa atributo, seguindo uma regra lógica (Ex: saldo não pode ser negativo)
print("Exercicío 1-")
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, valor):
        if valor < 0:
            print("Saldo não pode ser negatio")
        else:
            self.__saldo = valor

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.__saldo:.2f}")
      
    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.__saldo:.2f}")
conta = ContaBancaria("Maria", 3000)

conta.depositar(500)   
conta.sacar(300)       
conta.sacar(200)      
conta.depositar(100) 
conta.sacar(2000)      

#exercicío 2-Crie uma classe, Pessoa, que tenha os atributos: nome,  data de nascimento,, cpf, identidade. 
#Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores
print("\nExercicío 2-")
class Pessoa:
    def __init__(self, nome, data_de_nasc, cpf, ident):
        self.nome = nome
        self.data_de_nasc = data_de_nasc
        self.__cpf = cpf
        self.__ident = ident
    def __str__(self):
        return f"Nome:{self.nome}\nData de nascimento:{self.data_de_nasc}\nCPF:{self.__cpf}\nIdentidade:{ self.__ident}"
    
    def get__cpf(self):
        return self.__cpf

    def set__cpf(self, valor):
        self.__cpf = valor

    def get__ident(self):
        return self.__ident

    def set__ident(self, valor):
        self.__ident= valor

pessoa = Pessoa("Ana", "15-05-1990", "123.456.789-00", "MG-12.345.678")
print(pessoa)

pessoa.set__cpf("987.654.321-00")
pessoa.set__ident("SP-87.654.321")
print("\nApós alteração:")
print(pessoa)
