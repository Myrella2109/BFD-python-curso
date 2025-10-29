#exercicío 1-
print("Exercicío 1-")
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Livro: {self.titulo} por {self.autor}"

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.livro_favorito = None  
    def associar_livro(self, livro):
        self.livro_favorito = livro

    def __str__(self):
        if self.livro_favorito:
            return f"Pessoa: {self.nome}, livro favorito: {self.livro_favorito}"
        else:
            return f"Pessoa: {self.nome}, sem livro favorito associado"

livro1 = Livro("1984", "George Orwell")
pessoa1 = Pessoa("João")

pessoa1.associar_livro(livro1)

print(pessoa1)
print(livro1) 



#exercicío 2-
print("\nExercicío 2-")
class Onibus:
    def __init__(self, numero, rota):
        self.numero = numero
        self.rota = rota

    def __str__(self):
        return f"Ônibus {self.numero}, rota: {self.rota}"

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def pegar_onibus(self, onibus):
        print(f"{self.nome} está pegando o {onibus}.")

    def __str__(self):
        return f"Aluno: {self.nome}"

onibus1 = Onibus(123, "Centro - Universidade")
aluno1 = Aluno("Maria")

aluno1.pegar_onibus(onibus1)


#exercicío 3-
print("\nExercicío 3-")
class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}"

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []  

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"Funcionários do departamento {self.nome}:")
        for func in self.funcionarios:
            print(f"  - {func}")

    def __str__(self):
        return f"Departamento: {self.nome} ({len(self.funcionarios)} funcionários)"

func1 = Funcionario("João", "Desenvolvedor")
func2 = Funcionario("Maria", "Designer")

dept = Departamento("TI")

dept.adicionar_funcionario(func1)
dept.adicionar_funcionario(func2)

dept.listar_funcionarios()
print(dept)



#exercicío 4-
print("\nExercicío 4-")
class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def __str__(self):
        return f"Jogador: {self.nome}, Posição: {self.posicao}"

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        print(f"Jogadores do time {self.nome}:")
        for jog in self.jogadores:
            print(f"  - {jog}")

    def __str__(self):
        return f"Time: {self.nome} ({len(self.jogadores)} jogadores)"

jog1 = Jogador("Pelé", "Atacante")
jog2 = Jogador("Maradona", "Meio-campo")

time = Time("Seleção Brasileira")

time.adicionar_jogador(jog1)
time.adicionar_jogador(jog2)

time.listar_jogadores()
print(time)




#exercicío 5-
print("\nExercicío 5-")
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        print(f"Motor {self.tipo} criado.")

    def __del__(self):
        print(f"Motor {self.tipo} destruído.")

    def __str__(self):
        return f"Motor: {self.tipo}"

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor("V8") 
        print(f"Carro {self.modelo} criado com {self.motor}.")

    def __del__(self):
        print(f"Carro {self.modelo} destruído.")

    def __str__(self):
        return f"Carro: {self.modelo} com {self.motor}"

print("- Criando carro...")
carro = Carro("Fusca")

print("- Apagando carro...")
del carro

print("- Fim da demonstração.")



#exercicío 6-
print("\nExercicío 6-")
class Comodo:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Cômodo: {self.nome}"

class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.comodos = [] 
        self.comodos.append(Comodo("Sala"))
        self.comodos.append(Comodo("Cozinha"))
        self.comodos.append(Comodo("Quarto"))
        self.comodos.append(Comodo("Banheiro"))
        
    def listar_comodos(self):
        print(f"Cômodos da casa em {self.endereco}:")
        for comodo in self.comodos:
            print(f"  - {comodo}")

    def __str__(self):
        return f"Casa: {self.endereco} ({len(self.comodos)} cômodos)"

print("Criando casa...")
casa = Casa("Rua das Flores, 123")

casa.listar_comodos()
print(casa)

