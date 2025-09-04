#exercicío 1-Crie uma função chamada saudacaoque imprime na tela a mensagem 
# "Olá, bem-vindo ao Python!" . Em seguida, chame a função no programa.
print("Exercicío 1-")
def saudacao(mensagem):
    nome = input("Digite o nome do usúario:")
    return  f"{mensagem} {nome}, bem-vindo ao Python!"
print(saudacao("Olá"))

#exercicío 2 -Crie uma função chamada dobro que recebe um número como parâmetro 
# e retorna o dobro desse número. 
# Teste chamando a função com diferentes valores.
print("\nExercicío 2-")
def dobro():
    numero =int(input("Digite um número:"))
    dobro_n = numero * 2
    return f"O dobro de {numero} é {dobro_n}"
print(dobro())

#exercicío 3 -Crie uma função chamada soma que receba dois números e retorne a soma deles.
#  Depois, use a função para somar 10 + 20.
print("\nExercicío 3-")
def somar():
    num1 = int(input("Digite o primeiro número:"))
    num2 = int(input("Digite o segundo número:"))
    soma = num1 + num2
    return f"A soma de {num1} com {num2} é {soma}"
print(somar())

#exercicío 4-Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:
#"Olá, [nome]!"
#Caso o nome não seja informado, mostre "Olá, visitante!".
print("\nExercicío 4-")
def mensagem(nome=None):
    if nome is None:
        nome = input("Digite o nome do usuário: ")
    if nome:
        return f"Olá, {nome}!"
    else:
        return "Olá, visitante!"
print(mensagem())  


#exercicío 5-Crie uma função chamada operacoes que receba dois números 
# e retorne a soma, a subtração e a multiplicação deles.
print("\nExercicío 5-")
def operacoes():
    num1 = int(input("Digite o primeiro número:"))
    num2 = int(input("Digite o segundo número:"))
    soma = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    return f"O resultado das operações de {num1} com {num2} é \nsoma = {soma} \nsubtração = {sub} \nmultplicação = {mult}"
print(operacoes())

#exercicío 6-Crie uma função chamada media que receba uma quantidade variável de números 
# e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.
print("\nExercicío 6-")
def media(*numeros):
    if len(numeros) == 0:
        return 0  
    return sum(numeros) / len(numeros)
qtd = int(input("Quantos números deseja digitar?"))
valores = []
for i in range(qtd):
    num = int(input(f"Digite o {i+1}° número:"))
    valores.append(num)
resul = media(*valores)
print(f"A média dos {qtd} números é: \n{resul:.2f}")


#exercicío 7- Crie uma função chamada dados_pessoais que receba informações de uma pessoa
#(nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha. 
print("\nExercicío 7-")
def dados_pessoais(**kwargs):
    dados = {}
    for chave in kwargs:
        valor = input(f"Digite {chave}: ")
        dados[chave] = valor
    
    print("\nDados informados:")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
print(dados_pessoais())


#exercicío 8-Crie uma função chamada calculadora que tenha dentro dela outras funções 
# (somar, subtrair, multiplicar, dividir). A função principal deve permitir 
# escolher a operação e retornar o resultado.
print("\nExercicío 8-")
def calcular(num1, num2, operacao):
    if operacao == "+":
      return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 != 0:
         return num1 / num2 
        else:
            return "Erro: divisão por zero"
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
operacao = input("Digite a operação desejada(+ = soma, - = sub., * = mult., / = divisão):").strip().lower()
resul = calcular(num1, num2, operacao)
print("O resultado da operação é:", resul)


#exercicío 9-
print("\nExercicío 9-")
def divisao(num1, num2):
    num1 = int(input("Digite o primeiro número:"))
    num2 = int(input("Digite o segundo número:"))
    if num2 != 0:
         return num1 / num2 
    else:
         return "Erro: divisão por zero"
    
def aplicar_operacao(num1, num2):
    num1 = int(input("Digite o primeiro número:"))
    num2 = int(input("Digite o segundo número:"))
    return f"A divisão com {num1} e {num2} é:"
print(aplicar_operacao( num1, num2, divisao))          
