class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
       return f"Nome:{self.nome}\nE-mail:{self.email}"
    
    def saudacao(self):
        return "\nOlá, usuário!!^u^"
    

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):  
        super().__init__(nome, email) 
        self.saldo = saldo 
    
    def saudacao(self):
        return "\nOlá, cliente!!^u^"
    
    def exibir_informacoes1(self):
        return f"Nome:{self.nome} \nE-mail:{self.email}\nSaldo do cliente: R$ {self.saldo:.2f}"

class Funcionario(Usuario):
    def __init__(self, nome, email, salar):
        super().__init__(nome, email)  
        self.salar = salar  
    
    def exibir_informacoes2(self):
        return f"Nome:{self.nome} \nE-mail:{self.email}\nSalario do funcionario: R$ {self.salar}"
    
class Gerente(Funcionario):
    def __init__(self, nome, email, salario, depart):
        super().__init__(nome, email, salario)  
        self.depart = depart 
    
    def exibir_informacoes3(self):
        return f"Nome:{self.nome} \nE-mail:{self.email}\nSalario do gerente: R$ {self.salar}\nDepartamento:{self.depart}"
    
usuar = Usuario("João", "joao@gmail.com")
print(usuar.saudacao())
print("--- Informações do Usuário ---")
print(usuar.exibir_informacoes())
    
clie = Cliente("Carla", "carla.csg@gmail.com", 3050.00)
print(clie.saudacao())
print("--- Informações do Cliente ---")
print(clie.exibir_informacoes1())

funcio = Funcionario("Pedro", "pedro@empresa.com", 4000.00)
print("\n--- Informações do Funcionário ---")
print(funcio.exibir_informacoes2())

geren = Gerente("Maria", "maria@empresa.com", 8000.00, "Vendas")
print("\n--- Informações do Gerente ---")
print(geren.exibir_informacoes3()) 


#Exercicíos 6 e 7:
print("\nExercicíos 6 e 7:")
class Autenticacao:
    def __init__(self, usuario):
        self.usuario = usuario
    
    def login(self):
        return f"Login realizado com sucesso para o usuário: \n- {self.usuario}"
    
    def status(self):
        print("- Autenticado")
 
class Permissao:
    def __init__(self, nivel):
        self.nivel = nivel
    
    def verificar_permissao(self, acao):
        if self.nivel == "ADM":
            return True
        return False
    
    def status(self):
        print("- Permissões verificadas")
    
class Administrador(Autenticacao, Permissao):
    def __init__(self, usuario, nivel):
        Autenticacao.__init__(self, usuario)
        Permissao.__init__(self, nivel)
    
    def __str__(self):
        return f"\n{super(Autenticacao, self).__str__()}\n{super(Permissao, self).__str__()}"

admin = Administrador("joao_cl0908", "- ADM")
print(Administrador.__mro__) 
print(admin.login())
print("Nível do Usuário:\n", admin.nivel)
print("Status:")
admin.status() 

