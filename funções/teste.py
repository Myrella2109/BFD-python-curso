def aplicar_operacao(operacao):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = operacao(num1, num2)
    
    return resultado

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

resultado = aplicar_operacao(dividir)
print("Resultado:", resultado)