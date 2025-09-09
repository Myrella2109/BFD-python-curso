#exercicío1-Crie uma classe chamada Pessoa que tenha os atributos nome e idade.
#Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
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

#exercicío2-Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:
# "Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.


#exercicío3-Crie uma classe Carro com os atributos marca, modelo e ano. 
# Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo} do ano de {self.ano}"
carro1 = Carro("Jeep", "Jeep Compass", 2025 )
print("Primeira opção:", carro1)
carro2 = Carro
    


# exercicío4-Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos
# (por exemplo, mudar o ano). Imprima antes e depois da alteração.

# exercicío5-Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método 
# depositar(valor) que aumenta o saldo e um método sacar(valor) 
# que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.

# exercicío6-Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for 
# bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.


# exercicío7-Crie uma classe Aluno com atributos nome e nota. 
# Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). 
# Crie alguns objetos Aluno e adicione-os à turma.

# exercicío8-Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, 
# apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.


# exercicío9-Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" 
# e atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.