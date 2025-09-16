#exercicío 1-Crie uma classe chamada Pessoa que tenha os atributos nome e idade.
#Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
print("Exercicío 1-")
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"
    
pes1 = Pessoa("Ana Alves", 27)
pes2 = Pessoa("Carlos Araujo", 38)
print(pes1)
print(pes2)

#ecExpanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:
# "Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.
print("\nExercicío 2-")
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pes1 = Pessoa("Ana Alves", 27)
pes2 = Pessoa("Carlos Araujo", 38)

pes1.apresentar()
pes2.apresentar()


#exercicío 3/4-Crie uma classe Carro com os atributos marca, modelo e ano. 
# Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.
#- Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos
# (por exemplo, mudar o ano). Imprima antes e depois da alteração.
print("\nExercicío 3 e 4-")
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def __str__(self):
        return f"\nMarca: {self.marca} \nModelo: {self.modelo} do ano de {self.ano}"
carro1 = Carro("Jeep", "Jeep Compass", 2025 )
print("Primeira opção-", carro1)
carro2 = Carro("Ford", "F-250", 2010)
print("\nSegunda opção-", carro2)
carro2.ano = 2015
print("\nSegunda opção modificada-", carro2)
carro3 = Carro("Volkswagen","Polo Track", 2023)
print("\nTerceira opção-", carro3)

#exercicío 5-Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método 
# depositar(valor) que aumenta o saldo e um método sacar(valor) 
# que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.
print("\nExercicío 5-")
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque deve ser positivo.")
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
conta = ContaBancaria("João", 100)

conta.depositar(50)   
conta.sacar(30)       
conta.sacar(200)      
conta.depositar(10) 
conta.sacar(20)      



#exercicío 6- Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for 
# bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.
print("\nExercicío 6-")
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito deve ser positivo.")


    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque deve ser positivo.")
            return False
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")
            return False
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
            return True

conta = ContaBancaria("João", 100)

conta.depositar(50)  
if conta.sacar(30):
    print("Saque efetuado com sucesso.")
else:
    print("Falha ao realizar saque.")

if conta.sacar(200):
    print("Saque efetuado com sucesso.")
else:
    print("Falha ao realizar saque.")

if conta.sacar(20):
    print("Saque efetuado com sucesso.")
else:
    print("Falha ao realizar saque.")

# exercicío 7/8-Crie uma classe Aluno com atributos nome e nota. 
# Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). 
# Crie alguns objetos Aluno e adicione-os à turma.
#-Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, 
# apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.
print("\nExercicío 7 e 8-")
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"{self.nome} - Nota: {self.nota}"

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno)

aluno1 = Aluno("João", 8.5)
aluno2 = Aluno("Maria", 9.0)
aluno3 = Aluno("Pedro", 7.5)
aluno4 = Aluno("Alice", 9.5)
aluno5 = Aluno("Carol", 10.0)
aluno6 = Aluno("Lucas", 7.0)
aluno7 = Aluno("Cauã", 10.0)

turma = Turma()

turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)
turma.adicionar_aluno(aluno4)
turma.adicionar_aluno(aluno5)
turma.adicionar_aluno(aluno6)
turma.adicionar_aluno(aluno7)

turma.listar_alunos()

# exercicío 9-Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" 
# e atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.
print("\nExercicío 9-")
class Cachorro:
    especie = "Canis familiaris"  
    def __init__(self, nome, idade):
        self.nome = nome           
        self.idade = idade     

    def __str__(self):
        return f"Especie: {self.especie}\nNome: {self.nome}\nIdade: {self.idade}"
         
dog = Cachorro("Rex", 5)
print(dog)
print("\n", Cachorro.especie)  
print(dog.especie)      

