from abc import ABC, abstractmethod

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
