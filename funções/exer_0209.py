#exercicío 1-Crie uma função chamada saudacaoque imprime na tela a mensagem "Olá, bem-vindo ao Python!" . Em seguida, chame a função no programa.
def saudacao(mensagem):
    nome = input("Digite o nome do usúario:")
    return  f"{mensagem} {nome}, bem-vindo ao Python!"
print(saudacao("Olá"))

#exercicío 2 -
def dobro(dobro_do_numero):
    numero =int(input("Digite um número:"))
    dobro_n = numero * 2
    return f"O dobro de {numero} é {dobro_n}"
print(dobro)