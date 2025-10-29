from abc import ABC, abstractmethod

#Exercicío 1 e 2
print("Exercicío 1 e 2-")
class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass  

class Cachorro(Animal):
    def falar(self):
        print("Au au!\n")  

class Gato(Animal):
    def falar(self):
        print("Miau!")  


cachorro = Cachorro()
print("O cachorro diz:")
cachorro.falar() 
    
   
gato = Gato()
print("O gato diz:")
gato.falar()  

try:
    animal = Animal() 
except TypeError as e:
    print(f"Erro ao tentar instanciar Animal: {e}")


#Exercicío 3 
print("\nExercicío 3-")
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)

if __name__ == "__main__":
    ret = Retangulo(5, 3) 
    print(f"Área do retângulo: {ret.area()}")
    print(f"Perímetro do retângulo: {ret.perimetro()}")



# Exercicío 4
print("\nExercicío 4-")
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def parar(self):
        pass


class Carro(Transporte):
    def mover(self):
        return "O carro está se movendo."


try:
    carro = Carro()  
except TypeError as e:
    print(f"Erro ao instanciar Carro: {e}")


class CarroCorrigido(Transporte):
    def mover(self):
        return "O carro está se movendo."
    
    def parar(self):
        return "O carro parou."

carro_corrigido = CarroCorrigido()
print(carro_corrigido.mover())   
print(carro_corrigido.parar())   
