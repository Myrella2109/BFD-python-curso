from abc import ABC, abstractmethod

#Exercicío 1
print("Exercicío 1-")
class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        return f"Pagamento de R$ {valor:.2f} processado via cartão de crédito."

class Boleto(Pagamento):
    def processar(self, valor):
        return f"Pagamento de R$ {valor:.2f} processado via boleto bancário."

if __name__ == "__main__":
    cartao = CartaoCredito()
    boleto = Boleto()
    
    valor = 150.00
    
    print(cartao.processar(valor))
    print(boleto.processar(valor))


#Exercicío 2
print("\nExercicío 2-")

class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def __init__(self):
        self.ligado = False
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return "Computador ligado."
        else:
            return "Computador já está ligado."
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            return "Computador desligado."
        else:
            return "Computador já está desligado."

if __name__ == "__main__":
    pc = Computador()
    
    print(pc.ligar())
    print(pc.desligar())
    print(pc.desligar())  
    print(pc.ligar())    


#Exercicío 3
print("\nExercicío 3-")

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo
    
    def imprimir(self):
        return f"Imprimindo relatório '{self.titulo}': {self.conteudo}"
    
    def exportar(self):
        return f"Exportando relatório '{self.titulo}' para PDF: {self.conteudo}"

if __name__ == "__main__":
    relatorio = Relatorio("Relatório Anual", "Conteúdo do relatório aqui...")
    
    print(relatorio.imprimir())
    print(relatorio.exportar())


#Exercicío 4
print("\nExercicío 4-")

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass
    
    @abstractmethod
    def buscar(self, id):
        pass

class RepositorioMemoria(Repositorio):
    def __init__(self):
        self.dados = {}  

    def salvar(self, objeto):
        self.dados[objeto.id] = objeto
        print(f"Objeto com ID {objeto.id} salvo na memória.")
    
def buscar(self, id):
        return self.dados.get(id, None)


#Corrigido

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass
    
    @abstractmethod
    def buscar(self, id):
        pass


class RepositorioMemoria(Repositorio):
    def __init__(self):
        self.dados = {} 
    
    def salvar(self, objeto):
        self.dados[objeto.id] = objeto
        print(f"Objeto com ID {objeto.id} salvo na memória.")
    
    def buscar(self, id):
       
        return self.dados.get(id, None)


class ExemploObjeto:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    
    def __str__(self):
        return f"Objeto(id={self.id}, nome='{self.nome}')"


repo = RepositorioMemoria()  
obj1 = ExemploObjeto(1, "Exemplo 1")
repo.salvar(obj1)  
obj_recuperado = repo.buscar(1)  
print(obj_recuperado)  
print(repo.buscar(2))  
