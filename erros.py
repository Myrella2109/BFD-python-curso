# exercicío 1-Escreva um programa que peça ao usuário para digitar um número. 
# Trate o erro caso ele digite algo que não seja um número inteiro.
print("Exercicío 1-")
while True:
    entrada = input("Digite um número inteiro: ")
    try:
        numero = int(entrada)
        print(f"Você digitou o número {numero}.")
        break  
    except ValueError:
        print("Erro: por favor, digite um número inteiro.")


#exercicío 2-Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, 
# exiba uma mensagem de erro.
print("\nExercicío 2-")
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
except ValueError:
    print("Erro: por favor, digite apenas números.")

#exercicío 3-Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, 
# mostre uma mensagem usando o bloco else.
print("\nExercicío 3-")
entrada = input("Digite um número inteiro: ")
try: 
        numero = int(entrada)
except ValueError:
        print("Erro: por favor, digite um número inteiro.")
else:
        print(f"Você digitou o número {numero}.")
     
     
#exercicío 4-Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). 
# Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.
print("\nExercicío 4-")
try:
    arquivo = open("dados.txt", "r")
    print("Arquivo aberto com sucesso.")
except FileNotFoundError:
    print("Arquivo 'dados.txt' não encontrado.")
finally:
    print("Encerrando o programa.")


#exercicío 5- Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. 
# Caso contrário, retorne o resultado da divisão.
print("\nExercicío 5-")
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b

try:
    a = int(input("Digite o dividendo: "))
    b = int(input("Digite o divisor: "))
    resultado = dividir(a, b)

except ValueError:
    print("Erro: por favor, digite números inteiros válidos.")
else:
    print(f"Resultado da divisão: {resultado}")

#exercicío 6- Crie uma exceção personalizada chamada IdadeInvalidaError. Depois, crie uma função cadastrar_idade(idade) 
# que lance essa exceção caso a idade seja negativa.
print("\nExercicío 6-")
class IdadeInvalidaError(Exception):
    pass
def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Idade não pode ser negativa.")
    return f"Idade {idade} cadastrada com sucesso."

try:
    idade = int(input("Digite a idade: "))
    resultado = cadastrar_idade(idade)
except ValueError:
    print("Erro: por favor, digite um número inteiro válido.")
except IdadeInvalidaError as e:
    print(f"Erro: {e}")
else:
    print(resultado)


#exercicío 7-Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:
# ValueError se o usuário digitar algo inválido
# ZeroDivisionError se tentar dividir por zero
print("\nExercicío 7-")
try:
    a = float(input("Digite o dividendo: "))
    b = float(input("Digite o divisor: "))
    resultado = a / b
except ValueError:
    print("Erro: por favor, digite números válidos.")
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
else:
    print(f"Resultado da divisão: {resultado}")


#exercicío 8-Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:
# try para a conversão,
# else para verificar se é par ou ímpar,
# finally para exibir "Fim do programa".
print("\nExercicío 8-")
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: por favor, digite um número inteiro válido.")
else:
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
finally:
    print("Fim do programa.")


# exercicío 9-Crie uma função sacar(saldo, valor) que:
# Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
# Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem
# apropriada ao usuário.
print("\nExercicío 9-")
class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
    return saldo - valor

saldo_atual = 1000

try:
    valor_saque = float(input("Digite o valor para sacar: "))
    novo_saldo = sacar(saldo_atual, valor_saque)
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
else:
    print(f"Saque realizado com sucesso! Novo saldo: R$ {novo_saldo:.2f}")
