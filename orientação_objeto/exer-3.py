class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
       return f"As informações do usuário são :\nNome:{self.nome} \nE-mail:{self.email}."

    def __str__(self):
        return f"Nome:{self.nome} \nE-mail:{self.email}."
    
    def saudacao():
        return "Olá, usuário"
    

class Cliente(Usuario):
   

cliente1 = Cliente("Carla", "carla.csg@gmail.com")
print(cliente1.exibir_informacoes())




